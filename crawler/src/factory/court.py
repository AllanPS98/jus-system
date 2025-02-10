from abc import ABC, abstractmethod
from requests import Session
from src.model.orm import Orm

class Court(ABC):
    name = 'base'

    def __init__(self):
        self.db = Orm()
        self.session = Session()
        super().__init__()

    @abstractmethod
    def get_process(self, payload):
        pass # pragma: no cover