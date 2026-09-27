import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'toolhub-default-dev-secret-key-2026')
    
    # SQLite fallback path for Vercel Serverless environment
    if os.getenv('VERCEL'):
        default_db = 'sqlite:////tmp/toolhub.db'
    else:
        default_db = 'sqlite:///toolhub.db'

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', default_db)
    
    # Fix Heroku/Render/Vercel postgres:// URI prefix if necessary
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # File upload limits (16MB max upload)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    
    # AI Service Configuration
    AI_PROVIDER = os.getenv('AI_PROVIDER', 'default')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    
    # Session Cookie Security
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = os.getenv('FLASK_ENV') == 'production' or bool(os.getenv('VERCEL'))

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    PREFERRED_URL_SCHEME = 'https'

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': Config
}
