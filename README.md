# Sistema de Saúde - vidaPlus

Bem-vindo à documentação do **vidaPlus**, um sistema de saúde simples, modular e eficiente, projetado para gerenciar usuários, pacientes, prontuários, agendamentos e consultas de telemedicina. Este sistema foi desenvolvido para atender clínicas, hospitais e profissionais da área de saúde, garantindo segurança e conformidade com a LGPD.

---

## 🚀 Funcionalidades Principais

- **Autenticação Segura**: Controle de acesso por meio de JWT (JSON Web Token).
- **Gerenciamento de Usuários**: Controle de diferentes níveis de acesso (administrador, médico, recepcionista e paciente).
- **Cadastro e Consulta de Pacientes**: Registro e consulta de informações pessoais e de saúde.
- **Prontuários Eletrônicos**: Registro de diagnósticos e tratamentos realizados por médicos.
- **Agendamento de Consultas**: Organização de compromissos entre médicos e pacientes.
- **Telemedicina** *(opcional)*: Suporte a consultas online para acesso remoto a pacientes.

---

## 🛠️ Tecnologias Utilizadas

- **Back-End**: [Python](https://www.python.org/) com [Flask](https://flask.palletsprojects.com/)
- **Banco de Dados**: [PostgreSQL](https://www.postgresql.org/)
- **Autenticação**: [JWT](https://jwt.io/)
- **Gerenciamento de Dependências**: [pip](https://pypi.org/project/pip/)
- **Testes de API**: [Postman](https://www.postman.com/)

---

## 📚 Pré-Requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- [Python 3.10+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- Gerenciador de Pacotes [pip](https://pip.pypa.io/en/stable/installation/)

---

## 🖥️ Como Configurar o Projeto

### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie e Ative um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o Banco de Dados
- Crie um banco de dados no PostgreSQL.
- Configure o arquivo `.env` com as variáveis de ambiente necessárias:
  ```env
  FLASK_APP=app.py
  FLASK_ENV=development
  DATABASE_URL=postgresql://usuario:senha@localhost/vidaPlus
  SECRET_KEY=sua_chave_secreta
  ```

### 5. Execute as Migrações
```bash
flask db upgrade
```

### 6. Inicie o Servidor
```bash
flask run
```

O servidor estará disponível em: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🧪 Testes

### Testando com Postman
1. Importe a coleção `vidaPlus.postman_collection.json` no Postman.
2. Configure a variável `base_url` para **http://127.0.0.1:5000**.
3. Teste os endpoints disponíveis (login, usuários, pacientes, prontuários, etc.).

---

## 📂 Estrutura do Projeto

```plaintext
.
├── app/
│   ├── controllers/    # Controladores das rotas
│   ├── models/         # Definições das tabelas e regras de negócio
│   ├── services/       # Lógica de negócios
│   ├── utils/          # Funções auxiliares
│   └── app.py          # Arquivo principal da aplicação
├── migrations/         # Migrações do banco de dados
├── tests/              # Testes automatizados
├── requirements.txt    # Dependências do projeto
├── .env                # Arquivo de configuração
└── README.md           # Documentação do projeto
```

---

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

## 👨‍💻 Contribuidores

- **Seu Nome** - [GitHub](https://github.com/seu-usuario)
- Outros Contribuidores (adicione conforme necessário)

---

## 📞 Contato

Caso tenha dúvidas ou sugestões, entre em contato:
- **E-mail**: [seu-email@dominio.com](mailto:seu-email@dominio.com)
- **GitHub Issues**: [Acesse aqui](https://github.com/seu-usuario/seu-repositorio/issues)