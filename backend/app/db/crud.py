# app/db/crud.py
from . import get_conn
import pymysql


# def save_conversion(jp_text, converted, tone_from, tone_to, latency_ms=None):
#     sql = """
#     INSERT INTO translations (jp_text, converted, tone_from, tone_to, latency_ms)
#     VALUES (%s, %s, %s, %s, %s)
#     """
#     conn = get_conn()
#     with conn.cursor() as cur:
#         cur.execute(sql, (jp_text, converted, tone_from, tone_to, latency_ms))
#     if not conn.get_autocommit():
#         conn.commit()

def save_conversion():
    # 모델 적용 전이라 정의만 
    pass
# 최근 변환 문장 read
def list_recent(limit=10):
    sql = "SELECT * FROM convert_logs ORDER BY id DESC LIMIT %s"
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(sql, (limit,))
        return cur.fetchall()

# db user 정보 일치 확인
def get_user(id, pswd):
    sql = """
    SELECT id
    FROM users
    WHERE email = %s AND password_hash = %s
    """
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (id, pswd))
            return cur.fetchone()
    except pymysql.err.IntegrityError:
        return {"error": "일치하는 로그인 정보가 없습니다."}
    
# db user 정보 create 
def add_user(email, pswd_hash):
    sql = "INSERT INTO users (email, password_hash) VALUES (%s, %s)"
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (email, pswd_hash))
        conn.commit()
        return {"message": "회원가입이 완료되었습니다. 로그인 해주세요."}
    except pymysql.err.IntegrityError:
        return {"error": "이미 존재하는 이메일입니다."}
