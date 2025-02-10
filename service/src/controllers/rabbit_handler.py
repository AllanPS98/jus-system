import uuid
from src.config import ApplicationConfig
import pika
import json

config_app = ApplicationConfig()

class RabbitHandler:

    def __init__(self):
        self.host = config_app.RABBITMQ_HOST
        self.port = config_app.RABBITMQ_PORT
        self.queue_name = config_app.task_default_queue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))

    def send_message(self, message):
        try:
            channel = self.connection.channel()
            channel.queue_declare(queue=self.queue_name, durable=True)
            message_json = json.dumps(message)
            message_with_celery_body = {
                "args": [message_json],
                "kwargs": {}
            }
            channel.basic_publish(
                exchange='',
                routing_key=self.queue_name,
                body=json.dumps(message_with_celery_body),
                properties=pika.BasicProperties(
                    delivery_mode=2,
                    headers={'id': str(uuid.uuid4()), 'task': 'src.tasks.crawl_process.crawl_process'},
                    content_type='application/json'
                )
            )
            self.connection.close()
        except Exception as e:
            raise e
