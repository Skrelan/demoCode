import logging
logging.basicConfig( 
	level=logging.DEBUG,
	format="[%(asctime)s] | [%(levelname)s] | %(message)s")

def create_listing(data,db):
	query_insert_into_unit = """
	INSERT INTO units (
		unit,
		size,
		bathrooms,
		bedrooms ,
		email,
		phone, 
		price,
		zip_code,
		building_id ) 
	VALUES ('{0}',{1},{2},{3},'{4}',{5},{6},{7},{8});
	"""

	querry_get_unit_id ="""
	SELECT id FROM units WHERE building_id = {0} and unit = '{1}'
	"""

	querry_get_building_id = """
	SELECT id FROM buildings WHERE building_address = '{0}'
	"""

	query_insert_into_building ="""
	INSERT INTO buildings(
		building_address)
	VALUES
	('{0}')
	"""

	required = ['zip_code','price','address','email']
	
	#######
	for item in required:
		if item not in data:
			return {"message":"missing data"}


	data['address'] = data['address'].lower()
	try:
		results = db.query(querry_get_building_id.format(
			data['address']
			))

		if not(results):
			db.query(query_insert_into_building.format(
				data['address']
				))
			results = db.query(querry_get_building_id.format(
			data['address']
			))
	except Exception as e:
		logging.exception(e)
		return {"message":e}
	# return {"message":"data added","id":results[0]}
	########
	

	data['building_id'] = results[0]['id']
	logging.warning(data['building_id'])
	try:
		results = db.query(query_insert_into_unit.format(
			data.get('unit',None),
			data.get('size',-1),
			data.get('bathrooms',-1),
			data.get('bedrooms',-1),
			data['email'],
			data.get('phone',-1),
			data['price'],
			data['zip_code'],
			data['building_id']	
			))
	except Exception as e:
		logging.exception(e)
		return {"message":e}

	results = db.query(querry_get_unit_id.format(data['building_id'],data.get('unit',None)))
	
	pkgd = {"message":"data added",
			"id":results[0][id]}
	return pkgd


# def add_to_buildings():
# 	pass

# def 