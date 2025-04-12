from functools import wraps
from flask import request, jsonify
import jwt
from app.models import Usuario
from app import db
from config import Config

def checar_permissao(nivel_necessario):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization", "").replace("Bearer ", "")
            if not token:
                return jsonify({"erro": "Token de autenticação não fornecido"}), 401
            try:
                dados = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
                usuario = Usuario.query.get(dados["id"])
                if usuario.nivel_acesso != nivel_necessario and usuario.nivel_acesso != "administrador_geral":
                    return jsonify({"erro": "Acesso negado"}), 403
            except Exception as e:
                return jsonify({"erro": "Token inválido ou expirado"}), 401
            return func(*args, **kwargs)
        return wrapper
    return decorator