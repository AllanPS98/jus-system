import unittest
from src.common.functions import get_court_by_process_number, get_uuid


class TestFunctions(unittest.TestCase):

    def test_get_court_by_process_number(self):
        result = get_court_by_process_number('0070337-91.2008.8.06.0001')
        self.assertEqual(result, 'tjce')
    
    def test_get_uuid(self):
        result = get_uuid()
        self.assertIsNotNone(result)
