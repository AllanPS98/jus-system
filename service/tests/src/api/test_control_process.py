import unittest
from fastapi.testclient import TestClient
from unittest.mock import patch
from src.main import app
from datetime import datetime

class TestControlProcessEndpoint(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    @patch('src.api.control_process.ControlProcessController')
    def test_get_control_process(self, mock_control_process):
        mock_control_process_data = {
            'control_process_id': '12345',
            'status': 'processing',
            'message': 'Processing',
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }

        mock_control_process().get_control_process.return_value = mock_control_process_data
        response = self.client.get("/api/control-process/12345")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['control_process_id'], '12345')
        self.assertEqual(data['status'], 'processing')
        self.assertEqual(data['message'], 'Processing')
        self.assertIn('created_at', data)
        self.assertIn('updated_at', data)