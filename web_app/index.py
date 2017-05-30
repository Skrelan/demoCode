import web
import json
import config.configs as configs
import libs.database as db_funcs
import logging

logging.basicConfig( 
	level=logging.DEBUG,
	format="[%(asctime)s] | [%(levelname)s] | %(message)s")

urls = ('/','Index',
		'/test','Test',
		'/create','Create')
app = web.application(urls, globals())
web.config.debug = True

C = configs.Configs()

try:
	db = web.database(dbn='postgres', db='postgres', user='postgres', pw=C.logins["postgres"])
	is_db_connected = True
except Exception as e:
	logging.error("database connection failed\n{0}\nAborting".format(e))
	is_db_connected = False

try:
	global_render = web.template.render('templates/')
	is_render_set = True
except :
	logging.error("render failed")
	is_render_set = False



class Index:
	def __init__(self):
		self.render = global_render
		logging.info(self.render);

	def GET(self,name=''):
		payload = {'name':name,'message':'Hello World'}
		logging.info(payload)
		t = range(0,10)
		results = db.query("Select * from users")
		return self.render.index("hello is cool",results)

	def POST(self):
		data = json.loads(web.data())
		logging.info(data)
		return 'found it/n'


class Test:
	def GET(self,name=''):
		return 'no'

	def POST(self):
		data = json.loads(web.data())
		logging.info(data)
		#result = db.insert("insert into users(last_name,first_name) values('{0}','{1}')".format('test','bot'))
		result = db.insert('users', first_name="Bob", last_name="Smith")
		

class Create:
	def POST(self):
		data = json.loads(web.data())
		logging.info(data)
		result = db_funcs.create_listing(data,db)
		logging.info(result)
		return json.dumps(result)

#web.header('Content-Type','text/html; charset=utf-8', unique=True) 
if __name__ == '__main__':
	if is_db_connected and is_render_set:
		app.run()
	else: 
		logging.error("db connected: {0}, render connected: {1}".format(
		is_db_connected, is_render_set))
