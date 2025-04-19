from app import db
from datetime import datetime

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    nivel_acesso = db.Column(db.String(20), nullable=False)  # Ex: 'administrador', 'medico'

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    telefone = db.Column(db.String(15), nullable=True)
    endereco = db.Column(db.String(200), nullable=True)

    # Configurar o relacionamento com exclusão em cascata
    prontuarios = db.relationship('Prontuario', backref='paciente', cascade="all, delete-orphan")
    agendamentos = db.relationship('Agendamento', backref='paciente', cascade="all, delete-orphan")

class Prontuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id', ondelete='CASCADE'), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id', ondelete='CASCADE'), nullable=False)
    data_horario = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default="pendente")