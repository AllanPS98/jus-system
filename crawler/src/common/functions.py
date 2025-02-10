from src.config import ApplicationConfig
import pytz
import uuid


config_app = ApplicationConfig()

def timezone_br():
    return pytz.timezone(config_app.timezone)

def get_court_by_process_number(process_number: str):
    court = process_number.split('.')[3]
    dict_court = {
        '02': 'tjal',
        '06': 'tjce',
    }
    return dict_court.get(court)

def get_uuid():
    return uuid.uuid4()