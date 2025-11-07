# backend/app/main.py
from pathlib import Path
from flask import Flask
from flask_cors import CORS
from app import create_app
from app.api.routes_api import api_bp  

BASE_DIR = Path(__file__).resolve().parents[2]   
FRONTEND_DIR = BASE_DIR / "frontend"

app = create_app() 
CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "http://127.0.0.1:5173"}})  


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
