from http.server import HTTPServer 

from app.services.property_services import PropertyHandler

server = HTTPServer(('127.0.0.1',8080), PropertyHandler)

try:
	print('Starting server, use <Ctrl-C> to stop')
	server.serve_forever()
except KeyboardInterrupt:
	pass
server.server_close()
