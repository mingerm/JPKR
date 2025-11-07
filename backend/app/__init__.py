from flask import Flask
from flask_cors import CORS
from .api.routes_api import api_bp  
from .config import Config
from .db import init_app as init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5173"]}})
    init_db(app)  # PyMySQL 연결 생명주기 등록
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
