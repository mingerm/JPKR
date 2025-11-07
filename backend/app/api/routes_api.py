# app/api/routes_api.py
from flask import Blueprint, jsonify, request, make_response
from ..service.nlp_model import infer_tone_convert
from ..db.crud import list_recent, add_user, get_user

api_bp = Blueprint("api", __name__)

# @api_bp.post("/convert")
# def convert():
#     data = request.get_json(force=True) or {}
#     user_id = request.cookies.get("user_id")
#     jp = data.get("text","").strip()
#     tone_from = data.get("from","auto")
#     tone_to = data.get("to","formal")

#     if not jp:
#         return jsonify({"error":"text is required"}), 400
#     user_id = request.cookies.get("user_id")

#     # 모델 학습 완료 후 적용 예정
#     out = infer_tone_convert(jp, tone_from, tone_to)

#     try:
#         save_conversion(jp, out["converted"], tone_from, tone_to, user_id=int(user_id))
#     except Exception as e:
#         print("log failed:", e)

#     return jsonify(out), 200


@api_bp.post("/convert")
def convert():
    # 모델 구현 전이라 정의만
    pass


@api_bp.get("/logs")
def logs():
    return jsonify(list_recent(10)), 200

@api_bp.post("/login")
def login():
    data = request.get_json(force=True) or {}
    user_id = data.get("id")
    pswd = data.get("pswd")

    if not user_id or not pswd:
        return jsonify({"error": "아이디와 비밀번호를 입력하세요."}), 400

    user = get_user(user_id, pswd)

    if not user:
        return jsonify({"error": "아이디 또는 비밀번호가 잘못되었습니다."}), 401

    resp = make_response(jsonify({
        "message": "로그인 성공",
        "user": {"id": user["id"], "email": user_id}
    }))
    resp.set_cookie(
        "user_id",                
        str(user["id"]),          
        httponly=True,            
        samesite="Lax",           
        max_age=60*60*24      
    )

    return resp, 200


@api_bp.post("/signup")
def signup():
    data = request.get_json(force=True) or {}
    user_id = data.get("id")
    pswd = data.get("pswd")

    if not user_id or not pswd:
        return jsonify({"error": "아이디와 비밀번호를 입력하세요."}), 400

    try:
        result = add_user(user_id, pswd)
        return jsonify(result), 200
    except Exception as e:
        print("Signup error:", e)
        return jsonify({"error": "회원가입 중 오류가 발생했습니다."}), 500
    
@api_bp.post("/logout")
def logout():
    resp = make_response(jsonify({"message": "로그아웃 성공"}))
    resp.set_cookie("user_id", "", expires=0)
    return resp, 200
