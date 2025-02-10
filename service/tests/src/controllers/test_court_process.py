import unittest
from unittest.mock import patch
from src.controllers.court_process import CourtProcessController
from src.model.control_process import ControlProcess
from src.model.court_process import CourtProcess

class TestCourtProcessController(unittest.TestCase):

    @property
    def __controller(self):
        return CourtProcessController()

    @patch('src.controllers.court_process.RabbitHandler')
    @patch('src.controllers.court_process.ControlProcessController')
    @patch('src.controllers.Orm')
    def test_crawl_process(self, mock_orm, mock_control, mock_rabbit):
        mock_orm().orm.session.query().filter.return_value = []
        mock_control().add.return_value = 'control_id'
        result = self.__controller.crawl_process('test')
        self.assertEqual(result, 'control_id')
        self.assertTrue(mock_control().add.called)
        self.assertTrue(mock_control().set_queued.called)
        self.assertTrue(mock_rabbit().send_message.called)
    
    @patch('src.controllers.court_process.RabbitHandler')
    @patch('src.controllers.court_process.ControlProcessController')
    @patch('src.controllers.Orm')
    def test_crawl_process_with_update(self, mock_orm, mock_control, mock_rabbit):
        mock_court_process = CourtProcess()
        mock_court_process.control_process_id = 'control_id'
        mock_orm().orm.session.query().filter.return_value = [mock_court_process]
        result = self.__controller.crawl_process('test')
        self.assertEqual(result, 'control_id')
        self.assertFalse(mock_control().add.called)
        self.assertTrue(mock_control().set_queued.called)
        self.assertTrue(mock_rabbit().send_message.called)
    
    @patch('src.controllers.Orm')
    def test_get_process(self, mock_orm):
        mock_court_process = CourtProcess()
        mock_court_process.control_process = ControlProcess()
        mock_orm().orm.session.query().filter().order_by().offset().limit.return_value = [mock_court_process]
        mock_orm().orm.session.query().filter().order_by().count.return_value = 1
        result = self.__controller.get_process(1, 1, 'process_number', 'test')
        self.assertEqual(result['total'], 1)
        self.assertEqual(result['last_page'], 1)
        self.assertIsInstance(result['data'], list)
        
