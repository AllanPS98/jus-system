import unittest
from src.main import app

class TestMain(unittest.TestCase):

    def test_app_initialization(self):
        routes = [route.path for route in app.routes]

        assert app.title is not None
        assert app.version is not None
        assert "/api/court-process/" in routes
        assert "/api/control-process/{control_process_id}" in routes