import unittest

from src.common.functions import timezone_br, get_uuid


class TestFunctions(unittest.TestCase):

    def test_timezone_br(self):
        timezone = timezone_br()
        self.assertEqual(timezone.zone, 'America/Sao_Paulo')
    
    def test_get_uuid(self):
        result = get_uuid()
        self.assertIsNotNone(result)