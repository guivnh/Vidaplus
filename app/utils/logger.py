import logging
import os

# Criar o diretório "logs" se não existir
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configuração do logger
logging.basicConfig(
    filename=os.path.join(log_dir, "auditoria.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Função para registrar eventos
def registrar_evento(usuario_id, acao, descricao=""):
    logging.info(f"Usuário ID: {usuario_id} - Ação: {acao} - Descrição: {descricao}")