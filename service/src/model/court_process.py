from src.model.control_process import ControlProcess
from src.config import ApplicationConfig
from src.model.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship
from src.common.functions import get_uuid

config_app = ApplicationConfig()

class CourtProcess(BaseModel):
    __tablename__ = 'court_process'

    court_process_id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: get_uuid(), unique=True, nullable=False)
    control_process_id = Column(UUID(as_uuid=True), ForeignKey('control_process.control_process_id'), index=True, nullable=False)
    court_name = Column(String)
    process_number = Column(String, index=True)
    degree = Column(Integer, index=True)
    process_class = Column(String)
    area = Column(String)
    subject = Column(String)
    distribution_date = Column(String)
    judge = Column(String)
    share_value = Column(String)
    parts = Column(JSONB)
    moves = Column(JSONB)

    control_process = relationship('ControlProcess')
    
    @property
    def __court_name(self):
        return self.court_name

    @__court_name.setter
    def __court_name(self, value):
        self.court_name = value
    
    @property
    def __process_number(self):
        return self.process_number
    
    @__process_number.setter
    def __process_number(self, value):
        self.process_number = value
    
    @property
    def __degree(self):
        return self.degree
    
    @__degree.setter
    def __degree(self, value):
        self.degree = value
    
    @property
    def __process_class(self):
        return self.process_class
    
    @__process_class.setter
    def __process_class(self, value):
        self.process_class = value
    
    @property
    def __area(self):
        return self.area
    
    @__area.setter
    def __area(self, value):
        self.area = value
    
    @property
    def __subject(self):
        return self.subject
    
    @__subject.setter
    def __subject(self, value):
        self.subject = value
    
    @property
    def __distribution_date(self):
        return self.distribution_date
    
    @__distribution_date.setter
    def __distribution_date(self, value):
        self.distribution_date = value
    
    @property
    def __judge(self):
        return self.judge
    
    @__judge.setter
    def __judge(self, value):
        self.judge = value
    
    @property
    def __share_value(self):
        return self.share_value
    
    @__share_value.setter
    def __share_value(self, value):
        self.share_value = value
    
    @property
    def __parts(self):
        return self.parts
    
    @__parts.setter
    def __parts(self, value):
        self.parts = value
    
    @property
    def __moves(self):
        return self.moves
    
    @__moves.setter
    def __moves(self, value):
        self.moves = value
    
    @property
    def __control_process(self):
        return self.control_process
    
    @__control_process.setter
    def __control_process(self, value):
        if not value or not isinstance(value, ControlProcess):
            raise Exception('Control process is required')
        self.control_process = value
    
    def set_params(self, params: dict):
        self.__court_name = params.get('court_name')
        self.__process_number = params.get('process_number')
        self.__degree = params.get('degree')
        self.__process_class = params.get('process_class')
        self.__area = params.get('area')
        self.__subject = params.get('subject')
        self.__distribution_date = params.get('distribution_date')
        self.__judge = params.get('judge')
        self.__share_value = params.get('share_value')
        self.__parts = params.get('parts')
        self.__moves = params.get('moves')
        self.__control_process = params.get('control_process')
    
    def get(self):
        return {
            'court_process_id': str(self.court_process_id),
            'control_process_id': str(self.__control_process.control_process_id),
            'court_name': self.__court_name,
            'process_number': self.__process_number,
            'degree': self.__degree,
            'process_class': self.__process_class,
            'area': self.__area,
            'subject': self.__subject,
            'distribution_date': self.__distribution_date,
            'judge': self.__judge,
            'share_value': self.__share_value,
            'parts': self.__parts,
            'moves': self.__moves,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
