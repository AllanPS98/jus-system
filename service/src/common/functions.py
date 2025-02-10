import uuid
from src.config import ApplicationConfig
import pytz

config_app = ApplicationConfig()

def timezone_br():
    return pytz.timezone(config_app.timezone)

def get_uuid():
    return uuid.uuid4()