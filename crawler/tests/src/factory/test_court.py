import unittest
from unittest.mock import patch, MagicMock
from src.model.orm import Orm
from src.factory.court import Court


class TestCourt(unittest.TestCase):

    @patch("src.factory.court.Orm")
    def test_court_initialization(self, mock_orm):
        mock_orm_instance = MagicMock()
        mock_orm.return_value = mock_orm_instance

        class ConcreteCourt(Court):
            def get_process(self, payload):
                return "mocked_process"

        court_instance = ConcreteCourt()

        mock_orm.assert_called_once()
        self.assertEqual(court_instance.db, mock_orm_instance)

    def test_cannot_instantiate_abstract_class(self):
        with self.assertRaises(TypeError) as context:
            Court()
        self.assertEqual(
            "Can't instantiate abstract class Court with abstract method get_process",
            str(context.exception),
        )

    @patch("src.factory.court.Orm")
    def test_subclass_method_implementation(self, mock_orm):
        class ConcreteCourt(Court):
            def get_process(self, payload):
                return {"process": payload}

        mock_orm_instance = MagicMock()
        mock_orm.return_value = mock_orm_instance

        court_instance = ConcreteCourt()
        result = court_instance.get_process({"key": "value"})

        self.assertEqual(result, {"process": {"key": "value"}})
        mock_orm.assert_called_once()
