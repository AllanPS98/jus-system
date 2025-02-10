import os


class ApplicationConfig:

    DB_USERNAME = os.getenv('DB_USERNAME', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
    DB_NAME = os.getenv('DB_NAME', 'postgres')
    DB_HOST = os.getenv('DB_HOST', 'host.docker.internal')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_STRING_URI = f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    TJAL_URL_FIRST_DEGREE = os.getenv('TJAL_URL_FIRST_DEGREE', 'https://www2.tjal.jus.br/cpopg/open.do')
    TJAL_URL_SEARCH_FIRST_DEGREE = os.getenv('TJAL_URL_SEARCH_FIRST_DEGREE', 'https://www2.tjal.jus.br/cpopg/search.do')
    TJAL_URL_SECOND_DEGREE = os.getenv('TJAL_URL_SECOND_DEGREE', 'https://www2.tjal.jus.br/cposg5/open.do')
    TJAL_URL_SEARCH_SECOND_DEGREE = os.getenv('TJAL_URL_SEARCH_SECOND_DEGREE', 'https://www2.tjal.jus.br/cposg5/search.do')
    TJAL_URL_SHOW_SECOND_DEGREE = os.getenv('TJAL_URL_SEARCH_SECOND_DEGREE', 'https://www2.tjal.jus.br/cposg5/show.do')

    TJCE_URL_FIRST_DEGREE = os.getenv('TJCE_URL_FIRST_DEGREE', 'https://esaj.tjce.jus.br/cpopg/open.do')
    TJCE_URL_SEARCH_FIRST_DEGREE = os.getenv('TJCE_URL_SEARCH_FIRST_DEGREE', 'https://esaj.tjce.jus.br/cpopg/search.do')
    TJCE_URL_SECOND_DEGREE = os.getenv('TJCE_URL_SECOND_DEGREE', 'https://esaj.tjce.jus.br/cposg5/open.do')
    TJCE_URL_SEARCH_SECOND_DEGREE = os.getenv('TJAL_URL_SEARCH_SECOND_DEGREE', 'https://esaj.tjce.jus.br/cposg5/search.do')
    TJCE_URL_SHOW_SECOND_DEGREE = os.getenv('TJAL_URL_SEARCH_SECOND_DEGREE', 'https://esaj.tjce.jus.br/cposg5/show.do')

    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'amqp://guest:guest@rabbitmq:5672//')
    CELERY_BACKEND_URL = os.getenv('CELERY_BACKEND_URL', 'rpc://')
    task_routes = {'src.tasks.crawl_process.crawl_process': {'queue': 'crawler'}}
    task_default_queue = 'crawler'
    timezone = 'America/Sao_Paulo'
    broker_connection_retry_on_startup = True
    task_serializer='json'
    accept_content=['json']
    result_serializer='json'