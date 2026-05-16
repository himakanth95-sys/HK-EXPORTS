"""Initialize Flask application."""
from flask import Flask
from app.database import init_db

def create_app(config_name='development'):
    """Application factory."""
    app = Flask(__name__)
    
    # Load configuration
    if config_name == 'production':
        from app.config import ProductionConfig
        app.config.from_object(ProductionConfig)
    elif config_name == 'testing':
        from app.config import TestingConfig
        app.config.from_object(TestingConfig)
    else:
        from app.config import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)
    
    # Initialize database
    with app.app_context():
        init_db()
    
    # Register blueprints
    from app.routes import auth_bp, main_bp, admin_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    
    return app
