import unittest
from src.config import ApplicationConfig

class TestApplicationConfig(unittest.TestCase):

    def test_config(self):
        
        config_app = ApplicationConfig()
        self.assertIn('postgresql+psycopg2://', config_app.DB_STRING_URI)
        self.assertEqual(config_app.task_default_queue, 'crawler')
        self.assertEqual(config_app.timezone, 'America/Sao_Paulo')