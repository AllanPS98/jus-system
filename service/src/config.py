import os


class ApplicationConfig:

    DB_USERNAME = os.getenv('DB_USERNAME', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
    DB_NAME = os.getenv('DB_NAME', 'postgres')
    DB_HOST = os.getenv('DB_HOST', 'host.docker.internal')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_STRING_URI = f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'rabbitmq')
    RABBITMQ_PORT = os.getenv('RABBITMQ_PORT', '5672')
    task_default_queue = 'crawler'
    timezone = 'America/Sao_Paulo'