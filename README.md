# Projeto Jus-System

## Descrição

Jus-System é um repositório que integra uma API, um crawler para extração de dados, um sistema de mensageria com RabbitMQ e um ambiente Docker Compose para facilitar a implantação.

## Tecnologias Utilizadas

- **Python** (FastAPI, Celery, Alembic)
- **RabbitMQ** (mensageria)
- **PostgreSQL** (banco de dados)
- **Docker e Docker Compose** (contêinerização e orquestração)

## Estrutura do Projeto

```
/
|-- service/   # Contém a API principal
|-- crawler/   # Contém o worker para extração de dados
|-- rabbitmq/  # Definições para o RabbitMQ
|-- docker-compose.yml  # Configuração dos contêineres
```

## Pré-requisitos

Certifique-se de ter instalado:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Como Rodar o Projeto

1. Clone o repositório:
   ```sh
   git clone https://github.com/seuusuario/juscrawler.git
   cd juscrawler
   ```
2. Suba os contêineres com Docker Compose:
   ```sh
   docker-compose up --build
   ```
3. A API estará disponível em `http://localhost:8000`
4. A interface do RabbitMQ pode ser acessada em `http://localhost:15672` (usuário: guest, senha: guest)

## Endpoints da API

- `GET /court-process` - Recebe as informações do processo
- `POST /court-process` - Aciona o crawler para extrair informações
- `GET /control-process` - Recebe as informações da execução da extração



