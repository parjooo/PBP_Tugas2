from multiprocessing.connection import Client
from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class TestCaseRespon(TestCase):
    def test_contoh_watchlist_url_exists(self):
        respon = Client().get("/mywatchlist/",)
        self.assertEqual(respon.status_code,200)
    
    def test_contoh_watchlist_html_url_exists(self):
        respon = Client().get("/mywatchlist/html/",)
        self.assertEqual(respon.status_code,200)

    def test_contoh_watchlist_json_url_exists(self):
        respon = Client().get("/mywatchlist/json/",)
        self.assertEqual(respon.status_code,200)

    def test_contoh_watchlist_xml_url_exists(self):
        respon = Client().get("/mywatchlist/xml/",)
        self.assertEqual(respon.status_code,200)