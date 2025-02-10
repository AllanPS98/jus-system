import unittest
from unittest.mock import patch
from src.tasks.crawl_process import crawl_process


class TestCrawlProcess(unittest.TestCase):

    @patch('src.tasks.crawl_process.CourtProcessController')
    def test_crawl_process(self, mock_controller):
        message = '''{"process_number": "122345", "id_process": "11111"}'''
        crawl_process(message)
        self.assertTrue(mock_controller().crawl_process.called)