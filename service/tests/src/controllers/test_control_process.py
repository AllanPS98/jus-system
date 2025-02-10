import unittest
from unittest.mock import patch
from src.controllers.control_process import ControlProcessController
from src.model.control_process import ControlProcess
from src.model.court_process import CourtProcess

class TestControlProcessController(unittest.TestCase):

    @property
    def __controller(self):
        return ControlProcessController()

    @patch('src.controllers.Orm')
    def test_add(self, mock_orm):
        result = self.__controller.add()
        self.assertIsNone(result, None)
        self.assertTrue(mock_orm().orm.add_object.called)
        
    @patch('src.controllers.Orm')
    def test_set_queued(self, mock_orm):
        mock_control_process = ControlProcess()
        mock_orm().orm.session.query().filter.return_value = [mock_control_process]
        self.__controller.set_queued('test')
        self.assertTrue(mock_orm().orm.commit.called)
        self.assertTrue(mock_orm().orm.remove_session.called)
    
    @patch('src.controllers.Orm')
    def test_get_control_process(self, mock_orm):
        mock_control_process = ControlProcess()
        mock_orm().orm.session.query().filter.return_value = [mock_control_process]
        result = self.__controller.get_control_process('test')
        self.assertIsInstance(result, dict)
        self.assertTrue(mock_orm().orm.remove_session.called)
        
