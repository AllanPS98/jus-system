import unittest
from unittest.mock import patch
from src.model.orm import Orm

class TestOrm(unittest.TestCase):

    @patch("src.model.orm.SrcOrm")
    def test_init(self, mock_src_orm):
        orm = Orm()
        self.assertIsNotNone(orm.orm)