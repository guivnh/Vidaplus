from flask import Blueprint, request, jsonify
from app import db
from app.models import Usuario
from app.utils.permissions import checar_permissao
from app.utils.logger import registrar_evento

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route("/", methods=["POST"])
@checar_permissao("administrador_geral")
def criar_usuario():
    try:
        # Log para verificar o cabeçalho e o conteúdo recebido
        print("Cabeçalhos recebidos:", request.headers)
        print("JSON bruto recebido:", request.data)

        # Obtém o JSON enviado na requisição
        dados = request.get_json()
        print("JSON decodificado:", dados)  # Log para verificar o JSON decodificado

        # Verifica se todos os campos obrigatórios estão presentes
        if not dados or not all(campo in dados for campo in ["nome", "email", "senha", "nivel_acesso"]):
            print("Erro: Dados inválidos ou incompletos.")  # Log de erro
            return jsonify({"erro": "Dados inválidos ou incompletos"}), 400

        # Cria o novo usuário com os dados recebidos
        novo_usuario = Usuario(
            nome=dados["nome"],
            email=dados["email"],
            senha=dados["senha"],  # É recomendável hashear a senha antes de salvar no banco
            nivel_acesso=dados["nivel_acesso"]
        )
        db.session.add(novo_usuario)
        db.session.commit()

        print("Usuário criado com sucesso.")  # Log de sucesso
        return jsonify({"mensagem": "Usuário criado com sucesso"}), 201

    except KeyError as e:
        print(f"Erro: Campo obrigatório ausente: {e.args[0]}")  # Log de erro
        return jsonify({"erro": f"Campo obrigatório ausente: {e.args[0]}"}), 400
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")  # Log de erro
        return jsonify({"erro": f"Erro inesperado: {str(e)}"}), 500