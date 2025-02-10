from src.model.control_process import CREATED, QUEUED, ControlProcess
from . import ControllerDefault

class ControlProcessController(ControllerDefault):

    def add(self):
        control_process = ControlProcess()
        control_process.set_params({
            'status': CREATED,
            'message': 'Created process control'
        })
        self.db.orm.add_object(control_process)
        return control_process.control_process_id
    
    def set_queued(self, control_process_id):
        query = self.db.orm.session.query(ControlProcess).filter(ControlProcess.control_process_id == control_process_id)
        control_process = None
        for item in query:
            control_process = item
        control_process.set_params({
            'status': QUEUED,
            'message': 'Process queued'
        })
        self.db.orm.commit()
        self.db.orm.remove_session()
    
    def get_control_process(self, control_process_id: str):
        query = self.db.orm.session.query(ControlProcess).filter(ControlProcess.control_process_id == control_process_id)
        result = None
        for item in query:
            result = item.get()
        self.db.orm.remove_session()
        return result
