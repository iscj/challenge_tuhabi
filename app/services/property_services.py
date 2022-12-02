from http.server import BaseHTTPRequestHandler

from urllib import parse
import json
import re

from app.models.property import PropertyModel


class PropertyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.router('/filter'):
			self.properties_filters()
		elif self.router('/'):
			self.properties_all()
		else:
			return self.http_error(404, "METHOD Not found")
	
	def properties_filters(self):
		filter = self.parse_urlargs()
		data_filters = PropertyModel().filters(filter)
		if len(data_filters) == 0 :
			return self.http_error(404, "Item not found")
		return self.response(200, data_filters)

	def properties_all(self):
		properties = PropertyModel().available()
		if len(properties) == 0:
			return self.http_error(404, "Item not found")
		return self.response(200, properties)

	def parse_urlargs(self):
		query = parse.parse_qs(parse.urlparse(self.path).query)
		return {k:v[0] if v and len(v) == 1 else v for k,v in query.items()}

	def http_error(self, status_code, detail):
		self.response(status_code, {"detail": detail})

	def response(self,status_code=200, data_response={}):
		self.send_response(status_code)
		self.send_header('Content-type','text/json')
		self.end_headers()
		self.wfile.write(json.dumps(data_response).encode())

	def router(self, route_map):
		self.prefix = "/properties"
		return re.search(self.prefix + route_map, self.path)
