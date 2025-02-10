import unittest
from unittest.mock import patch
from src.controllers.court_process import CourtProcessController
from src.model.control_process import ControlProcess
from src.model.court_process import CourtProcess

class TestCourtProcess(unittest.TestCase):

    @property
    def __controller(self):
        return CourtProcessController()

    @patch('src.controllers.court_process.CourtFactory')
    @patch('src.controllers.court_process.get_court_by_process_number')
    @patch('src.controllers.court_process.ControlProcessController')
    @patch('src.controllers.Orm')
    def test_crawl_process(self, mock_orm, mock_control_controller, mock_get_court, mock_factory):
        control_process = ControlProcess()
        params = {
            'court_name': 'tjce',
            'process_number': '0070337-91.2008.8.06.0001',
            'degree': 1,
            'process_class': 'test',
            'area': 'test',
            'subject': 'test',
            'distribution_date': 'test',
            'judge': 'test',
            'share_value': 'test',
            'parts': [{'test': 'test'}],
            'moves': [{'test': 'test'}],
        }
        params2 = {
            'court_name': 'tjce',
            'process_number': '0070337-91.2008.8.06.0001',
            'degree': 2,
            'process_class': 'test',
            'area': 'test',
            'subject': 'test',
            'distribution_date': 'test',
            'judge': 'test',
            'share_value': 'test',
            'parts': [{'test': 'test'}],
            'moves': [{'test': 'test'}],
        }
        mock_get_court.return_value = 'tjce'
        mock_factory.get_instance().get_process.return_value = [
            params, params2
        ]
        mock_control_controller().get_instance.return_value = control_process
        mock_orm().orm.session.query().filter.side_effect = [[CourtProcess()], []]
        self.__controller.crawl_process('0070337-91.2008.8.06.0001', '11111')
        self.assertTrue(mock_control_controller().set_done.called)
    
    @patch('src.controllers.court_process.CourtFactory')
    @patch('src.controllers.court_process.get_court_by_process_number')
    @patch('src.controllers.court_process.ControlProcessController')
    @patch('src.controllers.Orm')
    def test_crawl_process_without_update(self, mock_orm, mock_control_controller, mock_get_court, mock_factory):
        control_process = ControlProcess()
        params = {
            'court_name': 'tjce',
            'process_number': '0070337-91.2008.8.06.0001',
            'degree': 1,
            'process_class': 'test',
            'area': 'test',
            'subject': 'test',
            'distribution_date': 'test',
            'judge': 'test',
            'share_value': 'test',
            'parts': [{'test': 'test'}],
            'moves': [{'test': 'test'}],
        }
        params2 = {
            'court_name': 'tjce',
            'process_number': '0070337-91.2008.8.06.0001',
            'degree': 2,
            'process_class': 'test',
            'area': 'test',
            'subject': 'test',
            'distribution_date': 'test',
            'judge': 'test',
            'share_value': 'test',
            'parts': [{'test': 'test'}],
            'moves': [{'test': 'test'}],
        }
        mock_get_court.return_value = 'tjce'
        mock_factory.get_instance().get_process.return_value = [
            params, params2
        ]
        mock_control_controller().get_instance.return_value = control_process
        mock_orm().orm.session.query().filter.side_effect = [[], []]
        self.__controller.crawl_process('0070337-91.2008.8.06.0001', '11111')
        self.assertTrue(mock_control_controller().set_done.called)
        self.assertTrue(mock_orm().orm.remove_session.called)
    
    @patch('src.controllers.court_process.CourtFactory')
    @patch('src.controllers.court_process.get_court_by_process_number')
    @patch('src.controllers.court_process.ControlProcessController')
    @patch('src.controllers.Orm')
    def test_crawl_process_error(self, mock_orm, mock_control_controller, mock_get_court, mock_factory):
        mock_get_court.return_value = None
        mock_factory.get_instance.side_effect = Exception
        self.__controller.crawl_process('0070337-91.2008.8.01.0001', '11111')
        self.assertTrue(mock_control_controller().set_error.called)
