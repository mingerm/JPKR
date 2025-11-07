# app/db/__init__.py
import pymysql
from flask import current_app, g

def get_conn():
    if "mysql_conn" not in g:
        g.mysql_conn = pymysql.connect(
            host=current_app.config["MYSQL_HOST"],
            port=current_app.config["MYSQL_PORT"],
            user=current_app.config["MYSQL_USER"],
            password=current_app.config["MYSQL_PASSWORD"],
            database=current_app.config["MYSQL_DB"],
            charset=current_app.config["MYSQL_CHARSET"],
            autocommit=current_app.config["MYSQL_AUTOCOMMIT"],
            cursorclass=pymysql.cursors.DictCursor, 
        )
    return g.mysql_conn

def close_conn(e=None):
    conn = g.pop("mysql_conn", None)
    if conn:
        try:
            conn.close()
        except pymysql.err.Error as ex:
            if "Already closed" not in str(ex):
                raise

def init_app(app):
    app.teardown_appcontext(close_conn)
