import math
from src.model.court_process import CourtProcess
from src.controllers.control_process import ControlProcessController
from . import ControllerDefault
from src.controllers.rabbit_handler import RabbitHandler
from sqlalchemy import desc

class CourtProcessController(ControllerDefault):

    @property
    def __control_process_controller(self):
        return ControlProcessController()
    
    @property
    def __rabbit_handler(self):
        return RabbitHandler()
    
    def __get_query(self, search_by, value):
        dict_search = {
            "process_id": self.db.orm.session.query(CourtProcess).filter(CourtProcess.control_process_id == value),
            "process_number": self.db.orm.session.query(CourtProcess).filter(CourtProcess.process_number == value)
        }
        return dict_search[search_by].order_by(desc(CourtProcess.created_at))
    
    def __check_is_update(self, process_number):
        query = self.db.orm.session.query(CourtProcess).filter(CourtProcess.process_number == process_number)
        control_process_id = None
        for item in query:
            control_process_id = item.control_process_id
            break
        self.db.orm.remove_session()
        return control_process_id

    def crawl_process(self, process_number):
        control_process_id = self.__check_is_update(process_number)
        if not control_process_id:
            control_process_id = self.__control_process_controller.add()
        message = {
            'control_process_id': str(control_process_id),
            'process_number': process_number
        }
        self.__rabbit_handler.send_message(message)
        self.__control_process_controller.set_queued(control_process_id)
        return control_process_id

    def get_process(self, page, amount, search_by, value):
        query = self.__get_query(search_by, value)
        total = query.count()
        last_page = math.ceil(total / amount)
        query = query.offset((page - 1) * amount).limit(amount)
        result = []
        for item in query:
            result.append(item.get())
        self.db.orm.remove_session()
        return {
            'total': total,
            'last_page': last_page,
            'data': result
        }