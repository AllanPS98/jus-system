from src.factory.tjal import Tjal
from src.factory.tjce import Tjce

__all__ = [Tjal, Tjce]

class CourtFactory:
    
    _instances = {}

    @staticmethod
    def get_instance(name):
        if name not in CourtFactory._instances:
            for court_class in __all__:
                if getattr(court_class, "name", None) == name:
                    CourtFactory._instances[name] = court_class()
                    break
            else:
                raise ValueError(f"Class not found: {name}")
        return CourtFactory._instances[name]