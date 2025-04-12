from flask import Blueprint, request, jsonify
from app import db
from app.models import Prontuario

prontuarios_bp = Blueprint('prontuarios', __name__)

@prontuarios_bp.route("/", methods=["GET"])
def listar_prontuarios():
    prontuarios = Prontuario.query.all()
    return jsonify([{"id": p.id, "paciente_id": p.paciente_id, "descricao": p.descricao, "data_criacao": p.data_criacao.isoformat()} for p in prontuarios])

@prontuarios_bp.route("/<int:prontuario_id>", methods=["GET"])
def obter_prontuario(prontuario_id):
    prontuario = Prontuario.query.get_or_404(prontuario_id)
    return jsonify({"id": prontuario.id, "paciente_id": prontuario.paciente_id, "descricao": prontuario.descricao, "data_criacao": prontuario.data_criacao.isoformat()})

@prontuarios_bp.route("/", methods=["POST"])
def criar_prontuario():
    dados = request.json
    novo_prontuario = Prontuario(
        paciente_id=dados["paciente_id"],
        descricao=dados["descricao"]
    )
    db.session.add(novo_prontuario)
    db.session.commit()
    return jsonify({"mensagem": "Prontuário criado com sucesso"}), 201