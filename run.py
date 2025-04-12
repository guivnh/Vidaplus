from flask_swagger_ui import get_swaggerui_blueprint
from app import create_app

# Criação da aplicação Flask
app = create_app()

# Configuração do Swagger para documentação da API
SWAGGER_URL = "/api/docs"  # URL para acessar a documentação
API_URL = "/static/swagger.json"  # Caminho para o arquivo JSON do Swagger

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Micro Sistema de Saúde VidaPlus",
        "validatorUrl": None  # Desativa o validador online para evitar problemas de rede
    }
)

# Registro do blueprint do Swagger
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Rota de fallback para tratar caminhos inválidos
@app.errorhandler(404)
def page_not_found(e):
    return {"erro": "Rota não encontrada. Verifique a URL e tente novamente."}, 404

# Inicialização do servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)