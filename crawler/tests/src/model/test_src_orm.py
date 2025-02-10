import unittest
from unittest.mock import MagicMock, patch
from src.model.src_orm import SrcOrm

class TestSrcOrm(unittest.TestCase):

    @patch("src.model.src_orm.create_engine")
    def test_init(self, mock_create_engine):
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        orm = SrcOrm("sqlite:///:memory:")
        self.assertIsNotNone(orm.session)

    @patch("src.model.src_orm.scoped_session")
    @patch("src.model.src_orm.create_engine")
    def test_add_object(self, mock_create_engine, mock_scoped_session):
        mock_engine = MagicMock()
        mock_session = MagicMock()
        mock_create_engine.return_value = mock_engine
        mock_scoped_session.return_value = mock_session

        orm = SrcOrm("sqlite:///:memory:")
        obj = MagicMock()
        orm.add_object(obj)

        mock_session.add.assert_called_once_with(obj)
        mock_session.commit.assert_called_once()

    @patch("src.model.src_orm.scoped_session")
    @patch("src.model.src_orm.create_engine")
    def test_commit_success(self, mock_create_engine, mock_scoped_session):
        mock_engine = MagicMock()
        mock_session = MagicMock()
        mock_create_engine.return_value = mock_engine
        mock_scoped_session.return_value = mock_session

        orm = SrcOrm("sqlite:///:memory:")
        orm.commit()

        mock_session.commit.assert_called_once()

    @patch("src.model.src_orm.scoped_session")
    @patch("src.model.src_orm.create_engine")
    def test_commit_exception(self, mock_create_engine, mock_scoped_session):
        mock_engine = MagicMock()
        mock_session = MagicMock()
        mock_create_engine.return_value = mock_engine
        mock_scoped_session.return_value = mock_session

        mock_session.commit.side_effect = Exception("Erro no commit")

        orm = SrcOrm("sqlite:///:memory:")
        with self.assertRaises(Exception) as context:
            orm.commit()
        self.assertEqual(str(context.exception), "Erro no commit")
        mock_session.rollback.assert_called_once()

    @patch("src.model.src_orm.scoped_session")
    @patch("src.model.src_orm.create_engine")
    def test_remove_session(self, mock_create_engine, mock_scoped_session):
        mock_engine = MagicMock()
        mock_session = MagicMock()
        mock_create_engine.return_value = mock_engine
        mock_scoped_session.return_value = mock_session

        orm = SrcOrm("sqlite:///:memory:")
        orm.remove_session()

        mock_session.remove.assert_called_once()

    @patch("src.model.src_orm.scoped_session")
    @patch("src.model.src_orm.create_engine")
    def test_close(self, mock_create_engine, mock_scoped_session):
        mock_engine = MagicMock()
        mock_session = MagicMock()
        mock_create_engine.return_value = mock_engine
        mock_scoped_session.return_value = mock_session

        orm = SrcOrm("sqlite:///:memory:")
        orm.close()

        mock_session.close.assert_called_once()