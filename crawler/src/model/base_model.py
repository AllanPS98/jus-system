from datetime import datetime
from src.config import ApplicationConfig
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from src.common.functions import timezone_br

config_app = ApplicationConfig()
Base = declarative_base()

class BaseModel(Base):

    __abstract__ = True
    created_at = Column(DateTime, default=datetime.now(timezone_br()))
    updated_at = Column(DateTime, default=datetime.now(timezone_br()), onupdate=datetime.now(timezone_br()))