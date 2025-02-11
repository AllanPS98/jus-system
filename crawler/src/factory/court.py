from abc import ABC, abstractmethod
from requests import Session
from src.model.orm import Orm

class Court(ABC):
    name = 'base'

    def __init__(self):
        self.db = Orm()
        self.session = Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "pt,pt-PT;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            
        }
        super().__init__()

    @abstractmethod
    def get_process(self, payload):
        pass # pragma: no cover