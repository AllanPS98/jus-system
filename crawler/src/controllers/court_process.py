import logging
from src.model.court_process import CourtProcess
from src.controllers.control_process import ControlProcessController
from . import ControllerDefault
from src.factory.court_factory import CourtFactory
from src.common.functions import get_court_by_process_number

log = logging.getLogger(__name__)

class CourtProcessController(ControllerDefault):

    @property
    def __control_process_controller(self):
        return ControlProcessController()

    def __add(self, control_process, item):
        court_process = CourtProcess()
        item['control_process'] = control_process
        court_process.set_params(item)
        self.db.orm.add_object(court_process)
    
    def __insert_in_database(self, court_processes, control_process):
        have_in_db = False
        for crawled_process in court_processes:
            query = self.db.orm.session.query(CourtProcess).filter(
                CourtProcess.process_number == crawled_process['process_number'],
                CourtProcess.degree == crawled_process['degree'], 
                CourtProcess.distribution_date == crawled_process['distribution_date']
            )
            result_query = None
            for item in query:
                have_in_db = True
                result_query = item
            if not result_query:
                self.__add(control_process, crawled_process)
                continue
            result_query.update(crawled_process)
            self.db.orm.commit()
        if not have_in_db:
            self.db.orm.remove_session()
    
    def crawl_process(self, process_number, control_process_id):
        self.__control_process_controller.set_processing(control_process_id)
        log.info(f'Processing court_process.process_numer: {process_number}')
        try:
            court = get_court_by_process_number(process_number)
            court_instance = CourtFactory.get_instance(court)
            court_processes = court_instance.get_process(process_number)
            log.info('Inserting crawler results in database')
            control_process = self.__control_process_controller.get_instance(control_process_id)
            self.__insert_in_database(court_processes, control_process)
            self.__control_process_controller.set_done(control_process_id)
            log.info(f'Finalized with success court_process.process_numer: {process_number}')
        except Exception as e:
            error_msg = f'Error in court_process.process_numer: {process_number} | {str(e)}'
            self.__control_process_controller.set_error(control_process_id, error_msg)
            log.info(f'Error in court_process.process_numer: {process_number}')
            log.info(f'control_process.id: {control_process_id}')
            log.info(f'Error message: {str(e)}')
