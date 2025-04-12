from flask import Blueprint, request, jsonify
from app import db
from app.models import Paciente

pacientes_bp = Blueprint('pacientes', __name__)

@pacientes_bp.route("/", methods=["GET"])
def listar_pacientes():
    pacientes = Paciente.query.all()
    return jsonify([{"id": p.id, "nome": p.nome, "data_nascimento": p.data_nascimento.isoformat()} for p in pacientes])

@pacientes_bp.route("/<int:paciente_id>", methods=["GET"])
def obter_paciente(paciente_id):
    paciente = Paciente.query.get_or_404(paciente_id)
    return jsonify({"id": paciente.id, "nome": paciente.nome, "data_nascimento": paciente.data_nascimento.isoformat()})

@pacientes_bp.route("/", methods=["POST"])
def criar_paciente():
    dados = request.json
    novo_paciente = Paciente(
        nome=dados["nome"],
        data_nascimento=dados["data_nascimento"],
        telefone=dados.get("telefone"),
        endereco=dados.get("endereco")
    )
    db.session.add(novo_paciente)
    db.session.commit()
    return jsonify({"mensagem": "Paciente criado com sucesso"}), 201

@pacientes_bp.route("/<int:paciente_id>", methods=["PUT"])
def atualizar_paciente(paciente_id):
    dados = request.json
    paciente = Paciente.query.get_or_404(paciente_id)
    paciente.nome = dados.get("nome", paciente.nome)
    paciente.data_nascimento = dados.get("data_nascimento", paciente.data_nascimento)
    paciente.telefone = dados.get("telefone", paciente.telefone)
    paciente.endereco = dados.get("endereco", paciente.endereco)
    db.session.commit()
    return jsonify({"mensagem": "Paciente atualizado com sucesso"})

@pacientes_bp.route("/<int:paciente_id>", methods=["DELETE"])
def excluir_paciente(paciente_id):
    paciente = Paciente.query.get_or_404(paciente_id)
    db.session.delete(paciente)
    db.session.commit()
    return jsonify({"mensagem": "Paciente excluído com sucesso"})