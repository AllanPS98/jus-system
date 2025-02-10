from src.config import ApplicationConfig
from src.model.src_orm import SrcOrm

config_app = ApplicationConfig()


class Orm:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Orm, cls).__new__(cls)
            cls._instance.__initialize()
        return cls._instance

    def __initialize(self):
        self.__orm = SrcOrm(config_app.DB_STRING_URI)
    
    @property
    def orm(self):
        return self.__orm