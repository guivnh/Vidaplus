from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from config import Config
from flask.json.provider import DefaultJSONProvider  # Importação correta para JSONEncoder

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__, static_folder="../static")
    app.config.from_object(config_class)

    # Configuração para suportar UTF-8 no JSON
    app.config["JSON_AS_ASCII"] = False

    # Substituir o provedor JSON padrão para garantir que caracteres UTF-8 não sejam escapados
    class CustomJSONProvider(DefaultJSONProvider):
        def dumps(self, obj, **kwargs):
            kwargs.setdefault("ensure_ascii", False)  # Garante exibição de caracteres UTF-8
            return super().dumps(obj, **kwargs)

        def loads(self, data, **kwargs):
            return super().loads(data, **kwargs)

    app.json = CustomJSONProvider(app)

    # Middleware para definir o cabeçalho de resposta como UTF-8
    @app.after_request
    def set_content_type(response):
        if response.content_type == "application/json":
            response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    # Inicializar extensões
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # Registrar blueprints
    from app.routes.auth import auth_bp
    from app.routes.usuarios import usuarios_bp
    from app.routes.pacientes import pacientes_bp
    from app.routes.prontuarios import prontuarios_bp
    from app.routes.agendamentos import agendamentos_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(usuarios_bp, url_prefix="/usuarios")
    app.register_blueprint(pacientes_bp, url_prefix="/pacientes")
    app.register_blueprint(prontuarios_bp, url_prefix="/prontuarios")
    app.register_blueprint(agendamentos_bp, url_prefix="/agendamentos")

    # Rota padrão para verificar se o servidor está funcionando
    @app.route("/", methods=["GET"])
    def index():
        return jsonify({"mensagem": "Bem-vindo à API do sistema VidaPlus!"}), 200

    return app