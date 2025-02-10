from src.config import ApplicationConfig
from src.model.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from src.common.functions import get_uuid

config_app = ApplicationConfig()
CREATED = 'created'
QUEUED = 'queued'
PROCESSING = 'processing'
DONE = 'done'
ERROR = 'error'

class ControlProcess(BaseModel):
    __tablename__ = 'control_process'

    control_process_id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: get_uuid(), unique=True, nullable=False)
    status = Column(String)
    message = Column(String)

    @property
    def __status(self):
        return self.status
    
    @__status.setter
    def __status(self, value):
        self.status = value
    
    @property
    def __message(self):
        return self.message
    
    @__message.setter
    def __message(self, value):
        self.message = value
    
    def set_params(self, params: dict):
        self.__status = params.get('status')
        self.__message = params.get('message')
    
    def get(self):
        return {
            'control_process_id': str(self.control_process_id),
            'status': self.__status,
            'message': self.__message,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }