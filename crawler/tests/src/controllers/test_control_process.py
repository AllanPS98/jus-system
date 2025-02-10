import unittest
from unittest.mock import patch
from src.controllers.control_process import ControlProcessController
from src.model.control_process import ControlProcess

class TestControlProcess(unittest.TestCase):

    @property
    def __controller(self):
        return ControlProcessController()

    @patch('src.controllers.Orm')
    def test_get_instance(self, mock_orm):
        mock_orm().orm.session.query().filter.return_value = [ControlProcess()]
        result = self.__controller.get_instance('11111')
        self.assertIsInstance(result, ControlProcess)
        self.assertTrue(mock_orm().orm.remove_session.called)
    
    @patch('src.controllers.Orm')
    def test_set_processing(self, mock_orm):
        mock_orm().orm.session.query().filter.return_value = [ControlProcess()]
        self.__controller.set_processing('11111')
        self.assertTrue(mock_orm().orm.commit.called)
        self.assertTrue(mock_orm().orm.remove_session.called)
    
    @patch('src.controllers.Orm')
    def test_set_done(self, mock_orm):
        mock_orm().orm.session.query().filter.return_value = [ControlProcess()]
        self.__controller.set_done('11111')
        self.assertTrue(mock_orm().orm.commit.called)
        self.assertTrue(mock_orm().orm.remove_session.called)
    
    @patch('src.controllers.Orm')
    def test_set_error(self, mock_orm):
        mock_orm().orm.session.query().filter.return_value = [ControlProcess()]
        self.__controller.set_error('11111', 'test error')
        self.assertTrue(mock_orm().orm.commit.called)
        self.assertTrue(mock_orm().orm.remove_session.called)
    
    
