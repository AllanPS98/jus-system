import unittest
from unittest.mock import patch, MagicMock
from src.factory.tjal import Tjal
from tests.src.factory.mock_html_tjal import tjal_first_degree_html, tjal_second_degree_html_1, tjal_second_degree_html_2
from tests.src.factory.mock_html_tjal import tjal_without
from tests.src.factory.mock_html_tjce import tjce_more_than_one_second_degree

class TestTjal(unittest.TestCase):

    @property
    def __crawler(self):
        return Tjal()

    @patch("src.factory.court.Session")
    def test_get_process(self, mock_session):
        mock_response1 = MagicMock()
        mock_response1.text = tjal_first_degree_html
        mock_response2 = MagicMock()
        mock_response2.text = tjal_second_degree_html_1
        mock_response3 = MagicMock()
        mock_response3.text = tjal_second_degree_html_2

        mock_session_instance = MagicMock()
        mock_session_instance.get.side_effect = [mock_response1, mock_response2, mock_response3]
        mock_session.return_value = mock_session_instance


        process_number = "0710802-55.2018.8.02.0001"

        result = self.__crawler.get_process(process_number)
        first_degree_result = result[0]
        second_degree_result = result[1]
        self.assertEqual(mock_session_instance.get.call_count, 3)
        self.assertEqual(first_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(first_degree_result["process_number"], process_number)
        self.assertEqual(first_degree_result["degree"], 1)
        self.assertEqual(first_degree_result["area"], 'Cível')
        self.assertEqual(first_degree_result["subject"], 'Dano Material')
        self.assertEqual(first_degree_result["distribution_date"], '02/05/2018 às 19:01 - Sorteio')
        self.assertEqual(first_degree_result["judge"], 'José Cícero Alves da Silva')
        self.assertEqual(first_degree_result["share_value"], 'R$281.178,42')

        self.assertEqual(second_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(second_degree_result["process_number"], process_number)
        self.assertEqual(second_degree_result["degree"], 2)
        self.assertEqual(second_degree_result["area"], 'Cível')
        self.assertEqual(second_degree_result["subject"], 'Obrigações')
        self.assertEqual(second_degree_result["distribution_date"], None)
        self.assertEqual(second_degree_result["judge"], None)
        self.assertEqual(second_degree_result["share_value"], '281.178,42')
    
    @patch("src.factory.court.Session") 
    def test_get_process_without_first_degree(self, mock_session):
        mock_response1 = MagicMock()
        mock_response1.text = tjal_without
        mock_response2 = MagicMock()
        mock_response2.text = tjal_second_degree_html_1
        mock_response3 = MagicMock()
        mock_response3.text = tjal_second_degree_html_2

        mock_session_instance = MagicMock()
        mock_session_instance.get.side_effect = [mock_response1, mock_response2, mock_response3]
        mock_session.return_value = mock_session_instance
        process_number = "0710802-55.2018.8.02.0001"

        result = self.__crawler.get_process(process_number)
        second_degree_result = result[0]

        self.assertEqual(mock_session_instance.get.call_count, 3)
        self.assertEqual(len(result), 1)
        self.assertEqual(second_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(second_degree_result["process_number"], process_number)
        self.assertEqual(second_degree_result["degree"], 2)
        self.assertEqual(second_degree_result["area"], 'Cível')
        self.assertEqual(second_degree_result["subject"], 'Obrigações')
        self.assertEqual(second_degree_result["distribution_date"], None)
        self.assertEqual(second_degree_result["judge"], None)
        self.assertEqual(second_degree_result["share_value"], '281.178,42')

    @patch("src.factory.court.Session")
    def test_get_process_without_second_degree(self, mock_session):
        mock_response1 = MagicMock()
        mock_response1.text = tjal_first_degree_html
        mock_response2 = MagicMock()
        mock_response2.text = tjal_without

        mock_session_instance = MagicMock()
        mock_session_instance.get.side_effect = [mock_response1, mock_response2]
        mock_session.return_value = mock_session_instance


        process_number = "0710802-55.2018.8.02.0001"

        result = self.__crawler.get_process(process_number)
        first_degree_result = result[0]
    
        self.assertEqual(mock_session_instance.get.call_count, 2)
        self.assertEqual(len(result), 1)
        self.assertEqual(first_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(first_degree_result["process_number"], process_number)
        self.assertEqual(first_degree_result["degree"], 1)
        self.assertEqual(first_degree_result["area"], 'Cível')
        self.assertEqual(first_degree_result["subject"], 'Dano Material')
        self.assertEqual(first_degree_result["distribution_date"], '02/05/2018 às 19:01 - Sorteio')
        self.assertEqual(first_degree_result["judge"], 'José Cícero Alves da Silva')
        self.assertEqual(first_degree_result["share_value"], 'R$281.178,42')

    @patch("src.factory.court.Session") 
    def test_get_process_second_degree_without_sublink(self, mock_session):
        mock_response1 = MagicMock()
        mock_response1.text = tjal_first_degree_html
        mock_response2 = MagicMock()
        mock_response2.text = tjal_second_degree_html_2

        mock_session_instance = MagicMock()
        mock_session_instance.get.side_effect = [mock_response1, mock_response2]
        mock_session.return_value = mock_session_instance


        process_number = "0710802-55.2018.8.02.0001"

        result = self.__crawler.get_process(process_number)
        first_degree_result = result[0]
        second_degree_result = result[1]
        self.assertEqual(mock_session_instance.get.call_count, 2)
        self.assertEqual(first_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(first_degree_result["process_number"], process_number)
        self.assertEqual(first_degree_result["degree"], 1)
        self.assertEqual(first_degree_result["area"], 'Cível')
        self.assertEqual(first_degree_result["subject"], 'Dano Material')
        self.assertEqual(first_degree_result["distribution_date"], '02/05/2018 às 19:01 - Sorteio')
        self.assertEqual(first_degree_result["judge"], 'José Cícero Alves da Silva')
        self.assertEqual(first_degree_result["share_value"], 'R$281.178,42')

        self.assertEqual(second_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(second_degree_result["process_number"], process_number)
        self.assertEqual(second_degree_result["degree"], 2)
        self.assertEqual(second_degree_result["area"], 'Cível')
        self.assertEqual(second_degree_result["subject"], 'Obrigações')
        self.assertEqual(second_degree_result["distribution_date"], None)
        self.assertEqual(second_degree_result["judge"], None)
        self.assertEqual(second_degree_result["share_value"], '281.178,42')
    
    @patch("src.factory.court.Session")
    def test_get_process_with_more_than_one_second_degree_process(self, mock_session):
        mock_response1 = MagicMock()
        mock_response1.text = tjal_first_degree_html
        mock_response2 = MagicMock()
        mock_response2.text = tjce_more_than_one_second_degree
        mock_response3 = MagicMock()
        mock_response3.text = tjal_second_degree_html_2

        mock_session_instance = MagicMock()
        mock_session_instance.get.side_effect = [mock_response1, mock_response2, mock_response3, mock_response3]
        mock_session.return_value = mock_session_instance

        process_number = "0710802-55.2018.8.02.0001"

        result = self.__crawler.get_process(process_number)
        first_degree_result = result[0]
        second_degree_result = result[1]
        self.assertEqual(mock_session_instance.get.call_count, 4)
        self.assertEqual(len(result), 3)
        self.assertEqual(first_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(first_degree_result["process_number"], process_number)
        self.assertEqual(first_degree_result["degree"], 1)
        self.assertEqual(first_degree_result["area"], 'Cível')
        self.assertEqual(first_degree_result["subject"], 'Dano Material')
        self.assertEqual(first_degree_result["distribution_date"], '02/05/2018 às 19:01 - Sorteio')
        self.assertEqual(first_degree_result["judge"], 'José Cícero Alves da Silva')
        self.assertEqual(first_degree_result["share_value"], 'R$281.178,42')

        self.assertEqual(second_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(second_degree_result["process_number"], process_number)
        self.assertEqual(second_degree_result["degree"], 2)
        self.assertEqual(second_degree_result["area"], 'Cível')
        self.assertEqual(second_degree_result["subject"], 'Obrigações')
        self.assertEqual(second_degree_result["distribution_date"], '31/10/2017 - 3ª Câmara Criminal')
        self.assertEqual(second_degree_result["judge"], None)
        self.assertEqual(second_degree_result["share_value"], '281.178,42')
