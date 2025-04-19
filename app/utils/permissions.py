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
            print(f"Token recebido: {token}")  # Log para verificar o token recebido

            if not token:
                return jsonify({"erro": "Token de autenticação não fornecido"}), 401

            try:
                # Decodificar o token JWT
                dados = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
                print(f"Token decodificado com sucesso: {dados}")

                # Buscar o usuário no banco
                usuario = Usuario.query.get(dados["id"])
                if not usuario:
                    print(f"Usuário com ID {dados['id']} não encontrado")
                    return jsonify({"erro": "Usuário não encontrado"}), 404

                # Verificar nível de acesso
                if usuario.nivel_acesso != nivel_necessario and usuario.nivel_acesso != "administrador_geral":
                    print(f"Acesso negado para o usuário {usuario.nome}")
                    return jsonify({"erro": "Acesso negado"}), 403

            except jwt.ExpiredSignatureError:
                print("Token expirado")
                return jsonify({"erro": "Token expirado"}), 401
            except jwt.InvalidTokenError as e:
                print(f"Token inválido: {e}")
                return jsonify({"erro": "Token inválido ou expirado"}), 401

            return func(*args, **kwargs)
        return wrapper
    return decorator