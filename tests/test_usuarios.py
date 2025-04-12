import unittest
from app import create_app, db
from app.models import Usuario

class TestUsuarios(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            usuario = Usuario(nome="Admin", email="admin@teste.com", senha="senha123", nivel_acesso="administrador_geral")
            db.session.add(usuario)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_listar_usuarios(self):
        response = self.client.get("/usuarios/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertGreater(len(data), 0)

    def test_criar_usuario(self):
        response = self.client.post("/usuarios/", json={
            "nome": "Novo Usuário", "email": "novo@teste.com", "senha": "senha123", "nivel_acesso": "medico"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("mensagem", response.get_json())