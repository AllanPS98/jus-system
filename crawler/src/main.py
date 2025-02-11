import json
from celery import Celery
from src.config import ApplicationConfig

config_app = ApplicationConfig()

app = Celery(
    config_app.task_default_queue,
    broker=config_app.CELERY_BROKER_URL,
    backend=config_app.CELERY_BACKEND_URL,
)
app.config_from_object(config_app)
import src.tasks.crawl_process



