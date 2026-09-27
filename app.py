import os
from flask import Flask, render_template, jsonify, request
from werkzeug.middleware.proxy_fix import ProxyFix
from config import config_by_name, Config
from extensions import db
from tool_registry import get_all_categories, get_all_tools

def create_app(config_class=None):
    env_name = os.getenv('FLASK_ENV', 'development')
    if config_class is None:
        config_class = config_by_name.get(env_name, Config)

    app = Flask(__name__)
    app.config.from_object(config_class)

    # ProxyFix middleware to handle reverse proxies (Nginx, Render, Cloudflare, Railway)
    app.wsgi_app = ProxyFix(
        app.wsgi_app,
        x_for=1,
        x_proto=1,
        x_host=1,
        x_port=1,
        x_prefix=1
    )

    # Initialize extensions
    db.init_app(app)

    # Register Blueprints
    from routes import main_bp, tools_bp, api_bp, auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(tools_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)

    # Global Jinja context variables
    @app.context_processor
    def inject_globals():
        return {
            'global_categories': get_all_categories(),
            'total_tools_count': len(get_all_tools())
        }

    # Production Security Headers
    @app.after_request
    def set_security_headers(response):
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        if request.is_secure:
            response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response

    # Custom Error Handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f"Internal Server Error: {error}")
        return render_template('errors/500.html'), 500

    # Auto-create database tables
    with app.app_context():
        import models  # ensure models are imported
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config.get('DEBUG', False))
