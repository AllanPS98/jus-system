from src.model.control_process import PROCESSING, DONE, ERROR, ControlProcess
from . import ControllerDefault

class ControlProcessController(ControllerDefault):
    
    def __update(self):
        self.db.orm.commit()
        self.db.orm.remove_session()
    
    def __get_instance(self, control_process_id):
        query = self.db.orm.session.query(ControlProcess).filter(ControlProcess.control_process_id == control_process_id)
        control_process = None
        for item in query:
            control_process = item
        return control_process
    
    def get_instance(self, control_process_id):
        query = self.db.orm.session.query(ControlProcess).filter(ControlProcess.control_process_id == control_process_id)
        control_process = None
        for item in query:
            control_process = item
        self.db.orm.remove_session()
        return control_process
    
    def set_processing(self, control_process_id):
        control_process = self.__get_instance(control_process_id)
        control_process.set_params({
            'status': PROCESSING,
            'message': 'Processing'
        })
        self.__update()
    
    def set_done(self, control_process_id):
        control_process = self.__get_instance(control_process_id)
        control_process.set_params({
            'status': DONE,
            'message': 'Success'
        })
        self.__update()

    def set_error(self, control_process_id, message):
        control_process = self.__get_instance(control_process_id)
        control_process.set_params({
            'status': ERROR,
            'message': message
        })
        self.__update()
    
