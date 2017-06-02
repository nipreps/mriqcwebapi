from eve.tests import TestMinimal
import os
import re
from flask_pymongo import MongoClient

url = 'mriqc_api'
MONGO_HOST = os.environ.get("MONGODB_HOST", 'mongodb'),
MONGO_PORT = int(os.environ.get("MONGODB_PORT", 27017))
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




