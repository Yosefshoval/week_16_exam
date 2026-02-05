import json
from pymongo import MongoClient
from os import getenv

MONGO_USER = getenv('MONGO_INITDB_ROOT_USERNAME')
MONGO_PASS = getenv('MONGO_INITDB_ROOT_PASSWORD')
mongo_uri = getenv("MONGO_URI", "mongodb://silent-payroll-mongo-svc:27017/")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")
file_path = r'employee_data_advanced.json'

print('# Making Connection')
myclient = MongoClient(mongo_uri)

print('# database')
db = myclient[mongo_db]

db.authenticate(MONGO_USER, MONGO_PASS)

print('# Created or Switched to collection')
Collection = db[mongo_collection]

print('# Loading or Opening the json file')
with open(file_path) as file:
    print
    file_data = json.load(file)

print('# Inserting the loaded data in the Collection')
ins_result = Collection.insert_many(file_data)
print('inserted')