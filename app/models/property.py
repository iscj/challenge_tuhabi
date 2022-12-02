from app.models.connection import Connection

class PropertyModel(Connection):
	def filters(self, filters):
		clause_sql = self.format_filters(filters)
		query_s = f"""SELECT 
										p.address, 
										p.city, 
										s.name as status, 
										p.price, 
										p.description
									FROM habi_db.property p
									INNER JOIN habi_db.status_history sh ON p.id=sh.property_id
									INNER JOIN habi_db.status s ON s.id=sh.status_id 
									WHERE sh.update_date IN(SELECT MAX(update_date) 
																						FROM habi_db.status_history 
																						GROUP BY property_id) 
																						AND (status_id=3 
																								OR status_id=4 
																								OR status_id=5) 
																						AND {clause_sql}"""
		data = self.execute(query_s)
		return data
		
	def available(self):
		query_s = f"""SELECT 
										p.address, 
										p.city, 
										s.name as status, 
										p.price, 
										p.description
								FROM property p
								INNER JOIN status_history sh ON p.id=sh.property_id
								INNER JOIN status s ON s.id=sh.status_id 
								WHERE sh.update_date IN(SELECT MAX(update_date) 
								FROM status_history 
								GROUP BY property_id) 
								AND (status_id=4 OR status_id=5)"""
		data = self.execute(query_s)
		return data

	def format_filters(self, filters):
		filter_valids = {"year": "p.year","city": "p.city", "status": "s.name"}
		filters = [f'{filter_valids.get(_filter)}=("{value}")'.replace(" ", "") 
							for _filter, value in filters.items() 
							if _filter in filter_valids.keys() and value != None]
		return " AND ".join(filters)
