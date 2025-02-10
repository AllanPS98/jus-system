import unittest
from unittest.mock import patch, MagicMock
from src.factory.court_factory import CourtFactory
from src.factory.tjal import Tjal
from src.factory.tjce import Tjce


class TestCourtFactory(unittest.TestCase):

    @patch("src.factory.court_factory.Tjal")
    @patch("src.factory.court_factory.Tjce")
    def test_get_instance_creates_new_instance(self, mock_tjce, mock_tjal):

        instance1 = CourtFactory.get_instance("tjal")
        instance2 = CourtFactory.get_instance("tjce")

        self.assertIsInstance(instance1, Tjal)
        self.assertIsInstance(instance2, Tjce)

    @patch("src.factory.court_factory.Tjal")
    def test_get_instance_reuses_existing_instance(self, mock_tjal):

        instance1 = CourtFactory.get_instance("tjal")
        instance2 = CourtFactory.get_instance("tjal")
        self.assertEqual(instance1, instance2)

    def test_get_instance_raises_error_for_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            CourtFactory.get_instance("InvalidName")
        self.assertEqual(str(context.exception), "Class not found: InvalidName")