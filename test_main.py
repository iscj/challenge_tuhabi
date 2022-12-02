import requests
import threading
from unittest import TestCase
from http.server import HTTPServer 

from app.services.property_services import PropertyHandler

class PropertiesTest(TestCase):
	def setUp(self):
		self.domain = '127.0.0.1'
		self.port = 8080
		self.url_base = f"http://{self.domain}:{self.port}"

	def test_filter_city(self):
		payload = {"city": "pereira"}
		response = requests.get(f"{self.url_base}/properties/filter", params=payload)
		filter_city_result = {
			"address": "Cll 1A #11B-20",
			"city": "pereira",
			"status": "vendido",
			"price": 300000000,
			"description": "hermoso acabado, listo para estrenar super comodo"
		}
		assert response.status_code == 200
		assert response.json()[0] == filter_city_result

	def test_filter_year(self):
		response = requests.get(f"{self.url_base}/properties/filter?year=2021")
		filter_year_result = {
			"address": "Malabar entrada 2",
			"city": "pereira",
			"status": "en_venta",
			"price": 350000000,
			"description": "Casa campestre con hermosos paisajes"
		}
		assert response.status_code == 200
		assert response.json()[0] == filter_year_result

	def test_all_filters_properties_error(self):
		response = requests.get(f"{self.url_base}/properties/filter?year=2011&city=medellin&status=vendido")
		assert response.status_code == 404
		assert response.json() == {"detail": "Item not found"}

if __name__ == '__main__':
	 unittest.main()