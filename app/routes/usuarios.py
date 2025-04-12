from flask import Blueprint, request, jsonify
from app import db
from app.models import Usuario
from app.utils.permissions import checar_permissao
from app.utils.logger import registrar_evento

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route("/", methods=["GET"])
@checar_permissao("administrador_geral")
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{"id": u.id, "nome": u.nome, "email": u.email, "nivel_acesso": u.nivel_acesso} for u in usuarios])

@usuarios_bp.route("/", methods=["POST"])
@checar_permissao("administrador_geral")
def criar_usuario():
    dados = request.json
    novo_usuario = Usuario(
        nome=dados["nome"],
        email=dados["email"],
        senha=dados["senha"],  # Adicionar hash da senha
        nivel_acesso=dados["nivel_acesso"]
    )
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuário criado com sucesso"}), 201

@usuarios_bp.route("/<int:usuario_id>", methods=["DELETE"])
@checar_permissao("administrador_geral")
def excluir_usuario(usuario_id):
    usuario = Usuario.query.get_or_404(usuario_id)
    db.session.delete(usuario)
    db.session.commit()
    registrar_evento(usuario_id, "Exclusão de usuário", f"Usuário {usuario.nome} foi excluído")
    return jsonify({"mensagem": "Usuário excluído com sucesso"})