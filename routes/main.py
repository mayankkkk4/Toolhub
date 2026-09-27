from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from tool_registry import (
    get_all_tools, get_all_categories, get_popular_tools,
    get_featured_tools, get_tools_by_category, get_category_by_id, search_tools
)
from models import Feedback, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    categories = get_all_categories()
    popular_tools = get_popular_tools()
    featured_tools = get_featured_tools()
    all_tools = get_all_tools()
    return render_template(
        'index.html',
        categories=categories,
        popular_tools=popular_tools,
        featured_tools=featured_tools,
        total_tools=len(all_tools)
    )

@main_bp.route('/tools')
def all_tools():
    categories = get_all_categories()
    tools = get_all_tools()
    category_id = request.args.get('category')
    selected_category = None
    if category_id:
        tools = get_tools_by_category(category_id)
        selected_category = get_category_by_id(category_id)
    return render_template(
        'tools_list.html',
        tools=tools,
        categories=categories,
        selected_category=selected_category
    )

@main_bp.route('/category/<category_id>')
def category_detail(category_id):
    category = get_category_by_id(category_id)
    if not category:
        return render_template('errors/404.html'), 404
    tools = get_tools_by_category(category_id)
    categories = get_all_categories()
    return render_template(
        'tools_list.html',
        tools=tools,
        categories=categories,
        selected_category=category
    )

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/docs')
def docs():
    return render_template('docs.html', tools=get_all_tools(), categories=get_all_categories())

@main_bp.route('/privacy')
def privacy():
    return render_template('privacy.html')

@main_bp.route('/terms')
def terms():
    return render_template('terms.html')

@main_bp.route('/status')
def status():
    return render_template('status.html')

@main_bp.route('/contribute', methods=['GET', 'POST'])
def contribute():
    if request.method == 'POST':
        feedback_type = request.form.get('feedback_type', 'suggestion')
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        email = request.form.get('email', '').strip() or None

        if title and description:
            fb = Feedback(
                feedback_type=feedback_type,
                title=title,
                description=description,
                email=email
            )
            db.session.add(fb)
            db.session.commit()
            return render_template('contribute.html', success=True)

    return render_template('contribute.html', success=False)

@main_bp.route('/sitemap.xml')
def sitemap():
    tools = get_all_tools()
    categories = get_all_categories()
    return render_template('sitemap.xml', tools=tools, categories=categories), 200, {'Content-Type': 'application/xml'}

@main_bp.route('/robots.txt')
def robots():
    return "User-agent: *\nAllow: /\nSitemap: /sitemap.xml\n", 200, {'Content-Type': 'text/plain'}
