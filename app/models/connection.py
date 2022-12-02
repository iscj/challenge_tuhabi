import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv

import os

load_dotenv()

config = {
	"user": os.getenv("USER_DB"),
	"password": os.environ.get("PASSWORD_DB"),
	"host": os.environ.get("HOST_DB"),
	"database": os.environ.get("DATABASE"),
	"port": os.environ.get("PORT_DB"),
	"raise_on_warnings": True
}
 # TODO: probar subir tiempo de espera
class Connection:
	def __init__(self):
		self.conect = self.get_conect()
		self.cursor = self.conect.cursor(dictionary=True)

	def execute(self, query, params=""):
		try:
			if params == "":
				self.cursor.execute(query)
			else:
				self.cursor.execute(query, [params])
			return self.cursor.fetchall()
		except Exception as e:
			print(e)
			return None
		finally:
			self.cursor.close()

	def get_conect(self):
		try:
			cnx = mysql.connector.connect(**config)
			return cnx
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)
		else:
			cnx.close()