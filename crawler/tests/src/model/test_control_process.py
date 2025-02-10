import unittest
from src.model.control_process import PROCESSING, ControlProcess


class TestCourtProcess(unittest.TestCase):

    def test_set_get(self):
        
        params = {
            'status': PROCESSING,
            'message': 'Processing'
        }
        control_process = ControlProcess()
        control_process.set_params(params)
        result = control_process.get()
        self.assertEqual(result['status'], params['status'])
        self.assertEqual(result['message'], params['message'])
    