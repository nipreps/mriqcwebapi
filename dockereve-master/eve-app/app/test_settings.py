from eve.tests import TestMinimal
import os
import re
from flask_pymongo import MongoClient

get_mongo_host = re.match('tcp://(.*):(.*)', os.environ['MONGODB_PORT'])
url = 'scenarios'
MONGO_HOST = get_mongo_host.group(1),
MONGO_PORT = int(get_mongo_host.group(2))
MONGO_DBNAME = 'test_DB'
class settingsTestCase(TestMinimal):
	def setUp(self):
		return super().setUp(settings_file = './settings.py')
	def dropDB(self):
		self.connection = MongoClient(MONGO_HOST,MONGO_PORT)
		self.connection.drop_database(MONGO_DBNAME)
		self.connection.close()
	def setupDB(self):
		self.connection = MongoClient(MONGO_HOST,MONGO_PORT)
		self.connection.drop_database(MONGO_DBNAME)
	def testGet(self):
		return_json,return_code = self.get(url)
		self.assert200(return_code)
	def testPost(self):
	 	return_json, return_code = self.post(url, {"cjv": 0.1231231})
	 	self.assertFalse(self.domain)
	 	self.assertFalse(return_json)
	 	# self.assert200(return_code)

# class settingsTestCase(TestMinimal):
# 	def dropDB(self):
# 		self.connection = MongoClient(MONGO_HOST, MONGO_PORT)
# 		self.connection.drop_database(MONGO_DBNAME)
# 		self.connection.close()

# 	def setupDB(self):
# 		self.connection = MongoClient(MONGO_HOST, MONGO_PORT)
# 		self.connection.drop_database(MONGO_DBNAME)
# 	def testPost():
#     	return_json, return_code = self.post(url,{"cjg":0.123123})
# 		print(return_json)
# 		print(return_code)




