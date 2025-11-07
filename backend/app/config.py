# backend/app/config.py
import os

# 환경 변수 
class Config:
    # Flask 내부 
    DEBUG = True
    TESTING = False

    # CORS 허용 도메인
    CORS_ORIGINS = ["http://localhost:5173"]

    # 모델 경로 (미정)
    # MODEL_PATH = "./weights"

    MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "0000")
    MYSQL_DB = os.getenv("MYSQL_DB", "jt")
    MYSQL_CHARSET = "utf8mb4"
    MYSQL_AUTOCOMMIT = True