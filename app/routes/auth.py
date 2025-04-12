from flask import Blueprint, request, jsonify
from app.models import Usuario
from app import db, bcrypt
from config import Config
import jwt
from datetime import datetime, timedelta

auth_bp = Blueprint('auth', __name__)

# Rota para login
@auth_bp.route("/login", methods=["POST"])
def login():
    """
    Realiza o login de um usuário com base no email e senha fornecidos.
    Retorna um token JWT se as credenciais forem válidas.
    """
    dados = request.json
    if not dados or "email" not in dados or "senha" not in dados:
        return jsonify({"erro": "Email e senha são obrigatórios"}), 400

    usuario = Usuario.query.filter_by(email=dados["email"]).first()

    if usuario and bcrypt.check_password_hash(usuario.senha, dados["senha"]):
        token = jwt.encode(
            {
                "id": usuario.id,
                "nome": usuario.nome,
                "exp": datetime.utcnow() + timedelta(hours=2),
            },
            Config.SECRET_KEY,
            algorithm="HS256",
        )
        return jsonify({
            "mensagem": "Login bem-sucedido",
            "token": token,
            "usuario": {
                "id": usuario.id,
                "nome": usuario.nome,
                "email": usuario.email,
            }
        }), 200

    return jsonify({"erro": "Credenciais inválidas"}), 401

# Rota para verificar se o serviço de autenticação está funcionando
@auth_bp.route("/", methods=["GET"])
def auth_index():
    """
    Rota principal do blueprint de autenticação.
    """
    return jsonify({"mensagem": "API de autenticação VidaPlus funcionando!"}), 200