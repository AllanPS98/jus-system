import unittest
from unittest.mock import patch, MagicMock
from src.factory.tjce import Tjce
from tests.src.factory.mock_html_tjce import tjce_first_degree_html, tjce_second_degree_html_1, tjce_second_degree_html_2
from tests.src.factory.mock_html_tjce import tjce_without, tjce_more_than_one_second_degree, tjce_process_with_all_fields

class TestTjce(unittest.TestCase):

    @property
    def __crawler(self):
        return Tjce()

    @patch("src.factory.court.Session")   
    def test_get_process(self, mock_session):
        mock_response1 = MagicMock()
        mock_response1.text = tjce_first_degree_html
        mock_response2 = MagicMock()
        mock_response2.text = tjce_second_degree_html_1
        mock_response3 = MagicMock()
        mock_response3.text = tjce_second_degree_html_2

        mock_session_instance = MagicMock()
        mock_session_instance.get.side_effect = [mock_response1, mock_response2, mock_response3]
        mock_session.return_value = mock_session_instance
        process_number = "0070337-91.2008.8.06.0001"

        result = self.__crawler.get_process(process_number)
        first_degree_result = result[0]
        second_degree_result = result[1]

        self.assertEqual(mock_session_instance.get.call_count, 3)
        self.assertEqual(len(result), 2)
        self.assertEqual(first_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(first_degree_result["process_number"], process_number)
        self.assertEqual(first_degree_result["degree"], 1)
        self.assertEqual(first_degree_result["area"], 'Criminal')
        self.assertEqual(first_degree_result["subject"], 'Crimes de Trânsito')
        self.assertEqual(first_degree_result["distribution_date"], '02/05/2018 às 09:13 - Sorteio')
        self.assertEqual(first_degree_result["judge"], None)
        self.assertEqual(first_degree_result["share_value"], None)

        self.assertEqual(second_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(second_degree_result["process_number"], process_number)
        self.assertEqual(second_degree_result["degree"], 2)
        self.assertEqual(second_degree_result["area"], 'Criminal')
        self.assertEqual(second_degree_result["subject"], 'Crimes de Trânsito')
        self.assertEqual(second_degree_result["distribution_date"], None)
        self.assertEqual(second_degree_result["judge"], None)
        self.assertEqual(second_degree_result["share_value"], None)
    
    @patch("src.factory.court.Session")   
    def test_get_process_without_first_degree(self, mock_session):
        mock_response1 = MagicMock()
        mock_response1.text = tjce_without
        mock_response2 = MagicMock()
        mock_response2.text = tjce_second_degree_html_2

        mock_session_instance = MagicMock()
        mock_session_instance.get.side_effect = [mock_response1, mock_response2]
        mock_session.return_value = mock_session_instance
        process_number = "0070337-91.2008.8.06.0001"

        result = self.__crawler.get_process(process_number)
        second_degree_result = result[0]

        self.assertEqual(mock_session_instance.get.call_count, 2)
        self.assertEqual(len(result), 1)
        self.assertEqual(second_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(second_degree_result["process_number"], process_number)
        self.assertEqual(second_degree_result["degree"], 2)
        self.assertEqual(second_degree_result["area"], 'Criminal')
        self.assertEqual(second_degree_result["subject"], 'Crimes de Trânsito')
        self.assertEqual(second_degree_result["distribution_date"], None)
        self.assertEqual(second_degree_result["judge"], None)
        self.assertEqual(second_degree_result["share_value"], None)
    
    @patch("src.factory.court.Session")   
    def test_get_process_without_second_degree(self, mock_session):
        mock_response1 = MagicMock()
        mock_response1.text = tjce_first_degree_html
        mock_response2 = MagicMock()
        mock_response2.text = tjce_without

        mock_session_instance = MagicMock()
        mock_session_instance.get.side_effect = [mock_response1, mock_response2]
        mock_session.return_value = mock_session_instance
        process_number = "0070337-91.2008.8.06.0001"

        result = self.__crawler.get_process(process_number)
        first_degree_result = result[0]
        self.assertEqual(mock_session_instance.get.call_count, 2)
        self.assertEqual(len(result), 1)
        self.assertEqual(first_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(first_degree_result["process_number"], process_number)
        self.assertEqual(first_degree_result["degree"], 1)
        self.assertEqual(first_degree_result["area"], 'Criminal')
        self.assertEqual(first_degree_result["subject"], 'Crimes de Trânsito')
        self.assertEqual(first_degree_result["distribution_date"], '02/05/2018 às 09:13 - Sorteio')
        self.assertEqual(first_degree_result["judge"], None)
        self.assertEqual(first_degree_result["share_value"], None)


    @patch("src.factory.court.Session")   
    def test_get_process_with_more_than_one_second_degree_process(self, mock_session):
        mock_response1 = MagicMock()
        mock_response1.text = tjce_first_degree_html
        mock_response2 = MagicMock()
        mock_response2.text = tjce_more_than_one_second_degree
        mock_response3 = MagicMock()
        mock_response3.text = tjce_second_degree_html_2

        mock_session_instance = MagicMock()
        mock_session_instance.get.side_effect = [mock_response1, mock_response2, mock_response3, mock_response3]
        mock_session.return_value = mock_session_instance
        process_number = "0070337-91.2008.8.06.0001"

        result = self.__crawler.get_process(process_number)
        first_degree_result = result[0]
        second_degree_result = result[1]

        self.assertEqual(mock_session_instance.get.call_count, 4)
        self.assertEqual(len(result), 3)
        self.assertEqual(first_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(first_degree_result["process_number"], process_number)
        self.assertEqual(first_degree_result["degree"], 1)
        self.assertEqual(first_degree_result["area"], 'Criminal')
        self.assertEqual(first_degree_result["subject"], 'Crimes de Trânsito')
        self.assertEqual(first_degree_result["distribution_date"], '02/05/2018 às 09:13 - Sorteio')
        self.assertEqual(first_degree_result["judge"], None)
        self.assertEqual(first_degree_result["share_value"], None)

        self.assertEqual(second_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(second_degree_result["process_number"], process_number)
        self.assertEqual(second_degree_result["degree"], 2)
        self.assertEqual(second_degree_result["area"], 'Criminal')
        self.assertEqual(second_degree_result["subject"], 'Crimes de Trânsito')
        self.assertEqual(second_degree_result["distribution_date"], '31/10/2017 - 3ª Câmara Criminal')
        self.assertEqual(second_degree_result["judge"], None)
        self.assertEqual(second_degree_result["share_value"], None)

    @patch("src.factory.court.Session")   
    def test_get_process_with_all_fields(self, mock_session):
        mock_response1 = MagicMock()
        mock_response1.text = tjce_process_with_all_fields
        mock_response2 = MagicMock()
        mock_response2.text = tjce_second_degree_html_1
        mock_response3 = MagicMock()
        mock_response3.text = tjce_second_degree_html_2

        mock_session_instance = MagicMock()
        mock_session_instance.get.side_effect = [mock_response1, mock_response2, mock_response3]
        mock_session.return_value = mock_session_instance
        process_number = "0070337-91.2008.8.06.0001"

        result = self.__crawler.get_process(process_number)
        first_degree_result = result[0]

        self.assertEqual(mock_session_instance.get.call_count, 3)
        self.assertEqual(len(result), 2)
        self.assertEqual(first_degree_result["court_name"], self.__crawler.name)
        self.assertEqual(first_degree_result["process_number"], process_number)
        self.assertEqual(first_degree_result["degree"], 1)
        self.assertEqual(first_degree_result["area"], 'Cível')
        self.assertEqual(first_degree_result["subject"], 'Desapropriação por Utilidade Pública / DL 3.365/1941')
        self.assertEqual(first_degree_result["distribution_date"], '17/02/2006 às 09:54 - Sorteio')
        self.assertEqual(first_degree_result["judge"], 'Hortênsio Augusto Pires Nogueira')
        self.assertEqual(first_degree_result["share_value"], 'R$1.000,00')
    
