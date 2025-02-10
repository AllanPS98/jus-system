from src.model.orm import Orm


class ControllerDefault:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ControllerDefault, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self.db = Orm()