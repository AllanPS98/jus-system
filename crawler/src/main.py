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



# def main():
#     print('Starting crawler')
#     from src.tasks.crawl_process import crawl_process
#     crawl_process(
#         json.dumps({
#             'process_number': '0813355-76.2024.8.02.0000',
#             'control_process_id': '78a4da03-d342-53f6-a071-e0f51b39e5ef'
#         })
#     )
#     # crawl_process(
#     #     json.dumps({
#     #         'process_number': '0070337-91.2008.8.06.0001',
#     #         'control_process_id': '814b8e65-4de7-5ebd-a805-01b9902556a9'
#     #     })
#     # )
#     # crawl_process(
#     #     json.dumps({
#     #         'process_number': '0050255-69.2020.8.06.0146',
#     #         'control_process_id': '814b8e65-4de7-5ebd-a805-01b9902556a9'
#     #     })
#     # )

# if __name__ == "__main__":
#     main()

# # 0638586-78.2024.8.06.0000 - nao tem primeiro grau
# # 0050255-69.2020.8.06.0146 - nao tem segundo grau
# # 0105299-54.2015.8.06.0112 - aparece uma lista de mais de um processo de segundo grau
# # 0090166-29.2006.8.06.0001 - aparece direto o segundo grau sem ter que selecionar