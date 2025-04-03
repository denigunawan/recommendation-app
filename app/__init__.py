
import os
from flask import Flask
from app.config import Config
from app.extensions import db, migrate
from app.routes import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inisiasi database & migration
    db.init_app(app)
    migrate.init_app(app,db)

    # Registrasi blue print routes
    app.register_blueprint(api_bp)
    
    return app