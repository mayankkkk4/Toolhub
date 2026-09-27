"""
Production WSGI Entrypoint for ToolHub.
Suitable for Gunicorn, uWSGI, Waitress, Render, Railway, or Nginx deployments.
"""
import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
