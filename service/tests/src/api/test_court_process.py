import unittest
from fastapi.testclient import TestClient
from unittest.mock import patch
from src.main import app
from datetime import datetime

class TestCourtProcessEndpoint(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)
    
    @patch('src.api.court_process.CourtProcessController')
    def test_create_court_process(self, mock_controller):
        payload = {
            "process_number": "0070337-91.2008.8.06.0001"
        }

        mock_controller().crawl_process.return_value = "12345"
        response = self.client.post("/api/court-process/", json=payload)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id_process'], "12345")

    @patch('src.api.court_process.CourtProcessController')
    def test_get_process(self, mock_controller):
        mock_process_data = {
            'data': [
            {
                    'court_process_id': '12345',
                    'control_process_id': '67890',
                    'court_name': 'Court A',
                    'process_number': '0070337-91.2008.8.06.0001',
                    'degree': 1,
                    'process_class': 'Class A',
                    'area': 'Civil',
                    'subject': 'Subject A',
                    'distribution_date': '12/08/2023',
                    'created_at': datetime.now(),
                    'updated_at': datetime.now()
                },
            ],
            'total': 1,
            'last_page': 1
        }

        mock_controller().get_process.return_value = mock_process_data
        response = self.client.get("/api/court-process/", params={"value": "0070337-91.2008.8.06.0001", "page": 1, "amount": 3, "search_by": "process_number"})
        data = response.json()
        court_process = data['data'][0]

        self.assertEqual(court_process['court_process_id'], '12345')
        self.assertEqual(court_process['control_process_id'], '67890')
        self.assertEqual(court_process['court_name'], 'Court A')
        self.assertEqual(court_process['process_number'], '0070337-91.2008.8.06.0001')
        self.assertEqual(court_process['degree'], 1)
        self.assertEqual(court_process['process_class'], 'Class A')
        self.assertEqual(court_process['area'], 'Civil')
        self.assertEqual(court_process['subject'], 'Subject A')
        self.assertEqual(court_process['distribution_date'], '12/08/2023')
        self.assertIn('created_at', court_process)
        self.assertIn('updated_at', court_process)