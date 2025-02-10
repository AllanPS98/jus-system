import unittest
from src.model.control_process import ControlProcess
from src.model.court_process import CourtProcess


class TestCourtProcess(unittest.TestCase):

    def test_set_get(self):
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
            'control_process': control_process
        }
        court_process = CourtProcess()
        court_process.set_params(params)
        result = court_process.get()
        self.assertEqual(result['court_name'], params['court_name'])
        self.assertEqual(result['process_number'], params['process_number'])
        self.assertEqual(result['degree'], params['degree'])
        self.assertEqual(result['process_class'], params['process_class'])
        self.assertEqual(result['area'], params['area'])
        self.assertEqual(result['subject'], params['subject'])
        self.assertEqual(result['distribution_date'], params['distribution_date'])
        self.assertEqual(result['share_value'], params['share_value'])
        self.assertEqual(result['parts'], params['parts'])
        self.assertEqual(result['moves'], params['moves'])
        self.assertIsInstance(court_process.control_process, ControlProcess)
    
    def test_set_error(self):
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
        court_process = CourtProcess()
        with self.assertRaises(Exception):
            court_process.set_params(params)