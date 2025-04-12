import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # Certifique-se de que esta linha está correta
    SQLALCHEMY_TRACK_MODIFICATIONS = False