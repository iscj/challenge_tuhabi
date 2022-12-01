from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_filter_city():
	response = client.get("/properties/filter?city=pereira")
	filter_city_result = {
		"address": "Cll 1A #11B-20",
		"city": "pereira",
		"status": "vendido",
		"price": 300000000,
		"description": "hermoso acabado, listo para estrenar super comodo"
	}
	assert response.status_code == 200
	assert response.json()[0] == filter_city_result

def test_filter_year():
	response = client.get("/properties/filter?year=2021")
	filter_year_result = {
		"address": "Malabar entrada 2",
		"city": "pereira",
		"status": "en_venta",
		"price": 350000000,
		"description": "Casa campestre con hermosos paisajes"
	}
	assert response.status_code == 200
	assert response.json()[0] == filter_year_result

def test_all_filters_properties_error():
	response = client.get("/properties/filter?year=2011&city=medellin&status=vendido")
	assert response.status_code == 404
	assert response.json() == {"detail": "Item not found"}