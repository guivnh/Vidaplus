from flask import Blueprint, request, jsonify
from app import db
from app.models import Agendamento

agendamentos_bp = Blueprint('agendamentos', __name__)

@agendamentos_bp.route("/", methods=["GET"])
def listar_agendamentos():
    """Lista todos os agendamentos."""
    agendamentos = Agendamento.query.all()
    return jsonify([{
        "id": a.id,
        "paciente_id": a.paciente_id,
        "data_horario": a.data_horario.isoformat(),
        "status": a.status
    } for a in agendamentos])

@agendamentos_bp.route("/<int:agendamento_id>", methods=["GET"])
def obter_agendamento(agendamento_id):
    """Obtém detalhes de um agendamento específico."""
    agendamento = Agendamento.query.get_or_404(agendamento_id)
    return jsonify({
        "id": agendamento.id,
        "paciente_id": agendamento.paciente_id,
        "data_horario": agendamento.data_horario.isoformat(),
        "status": agendamento.status
    })

@agendamentos_bp.route("/", methods=["POST"])
def criar_agendamento():
    """Cria um novo agendamento."""
    dados = request.json
    novo_agendamento = Agendamento(
        paciente_id=dados["paciente_id"],
        data_horario=dados["data_horario"],
        status=dados.get("status", "pendente")
    )
    db.session.add(novo_agendamento)
    db.session.commit()
    return jsonify({"mensagem": "Agendamento criado com sucesso"}), 201

@agendamentos_bp.route("/<int:agendamento_id>", methods=["PUT"])
def atualizar_agendamento(agendamento_id):
    """Atualiza um agendamento existente."""
    dados = request.json
    agendamento = Agendamento.query.get_or_404(agendamento_id)
    agendamento.data_horario = dados.get("data_horario", agendamento.data_horario)
    agendamento.status = dados.get("status", agendamento.status)
    db.session.commit()
    return jsonify({"mensagem": "Agendamento atualizado com sucesso"})

@agendamentos_bp.route("/<int:agendamento_id>", methods=["DELETE"])
def excluir_agendamento(agendamento_id):
    """Exclui um agendamento."""
    agendamento = Agendamento.query.get_or_404(agendamento_id)
    db.session.delete(agendamento)
    db.session.commit()
    return jsonify({"mensagem": "Agendamento excluído com sucesso"})