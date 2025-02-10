import json
import logging
from src.main import app
from src.controllers.court_process import CourtProcessController

log = logging.getLogger(__name__)

@app.task
def crawl_process(message):
    payload = json.loads(message)
    process_number = payload.get('process_number')
    control_process_id = payload.get('control_process_id')
    log.info(f'Received message success: {message}')
    controller = CourtProcessController()
    controller.crawl_process(process_number, control_process_id)