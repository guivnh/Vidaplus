import unittest
from app import create_app, db
from app.models import Usuario
from flask_bcrypt import generate_password_hash

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            senha_hash = generate_password_hash("senha123").decode("utf-8")
            usuario = Usuario(nome="Admin", email="admin@teste.com", senha=senha_hash, nivel_acesso="administrador_geral")
            db.session.add(usuario)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login(self):
        response = self.client.post("/auth/login", json={"email": "admin@teste.com", "senha": "senha123"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.get_json())

    def test_login_invalido(self):
        response = self.client.post("/auth/login", json={"email": "admin@teste.com", "senha": "senha_errada"})
        self.assertEqual(response.status_code, 401)
        self.assertIn("erro", response.get_json())