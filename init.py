from app import create_app, db
from app.models import Usuario

app = create_app()

with app.app_context():
    db.create_all()

    # Adicionar um administrador padrão
    if not Usuario.query.filter_by(email="admin@teste.com").first():
        from flask_bcrypt import generate_password_hash
        senha_hash = generate_password_hash("admin123").decode("utf-8")
        usuario = Usuario(nome="Admin", email="admin@teste.com", senha=senha_hash, nivel_acesso="administrador_geral")
        db.session.add(usuario)
        db.session.commit()

print("Banco de dados inicializado com sucesso!")