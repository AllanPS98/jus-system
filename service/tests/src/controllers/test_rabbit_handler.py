import unittest
from src.controllers.rabbit_handler import RabbitHandler
from unittest.mock import patch

class TestRabbitHandler(unittest.TestCase):

    @patch('src.controllers.rabbit_handler.pika')
    def test_send_message(self, mock_pika):
        rabbit_handler = RabbitHandler()
        rabbit_handler.send_message({'process_number': 'test'})
        self.assertTrue(mock_pika.BlockingConnection.called)
    
    @patch('src.controllers.rabbit_handler.pika')
    def test_send_message_error(self, mock_pika):
        rabbit_handler = RabbitHandler()
        mock_pika.BlockingConnection().channel.side_effect = Exception
        with self.assertRaises(Exception):
            rabbit_handler.send_message({'process_number': 'test'})