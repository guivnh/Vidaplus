from flask import Blueprint, request, jsonify
from app.models import Usuario
from app import db, bcrypt
from config import Config
import jwt  # Certifique-se de que é o módulo PyJWT
from datetime import datetime, timedelta

# Alteração do nome do blueprint para garantir que seja único
auth_bp = Blueprint('auth_blueprint', __name__)

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
        # Gera o token JWT
        token = jwt.encode(
            {
                "id": usuario.id,
                "nome": usuario.nome,
                "exp": datetime.utcnow() + timedelta(hours=2),  # Expiração do token
            },
            Config.SECRET_KEY,  # Chave secreta para assinatura do token
            algorithm="HS256"  # Algoritmo de assinatura
        )

        # Retorna o token e os dados do usuário
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
@auth_bp.route("/status", methods=["GET"])
def auth_status():
    """
    Rota de status do serviço de autenticação.
    """
    return jsonify({"mensagem": "API de autenticação VidaPlus funcionando!"}), 200