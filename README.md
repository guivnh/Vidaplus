# Sistema de Saúde - vidaPlus

Documentação do **VidaPlus**

Um sistema de saúde simples, modular e eficiente, projetado para gerenciar usuários, pacientes, prontuários, agendamentos e consultas de telemedicina. Este sistema foi desenvolvido para atender clínicas, hospitais e profissionais da área de saúde, garantindo segurança e conformidade com a LGPD.

---

## 🚀 Funcionalidades Principais

- **Autenticação Segura**: Controle de acesso por meio de JWT (JSON Web Token).
- **Gerenciamento de Usuários**: Controle de diferentes níveis de acesso (administrador, médico, recepcionista e paciente).
- **Cadastro e Consulta de Pacientes**: Registro e consulta de informações pessoais e de saúde.
- **Prontuários Eletrônicos**: Registro de diagnósticos e tratamentos realizados por médicos.
- **Agendamento de Consultas**: Organização de compromissos entre médicos e pacientes.

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
git clone https://github.com/guivnh/Vidaplus.git
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
- Crie uma database no PostgreSQL chamada 'micro_sistema_saude' e as tabelas: 'agendamento', 'paciente', 'prontuário' e 'usuario'.
- Configure o arquivo `.env` com as variáveis de ambiente necessárias:
  ```env
  FLASK_APP=app.py
  FLASK_ENV=development
  DATABASE_URL=postgresql://postgres:!Root1@localhost/micro_sistema_saude
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

## 📄 Licença

Este projeto está licenciado sob a Apache License 2.0.

---