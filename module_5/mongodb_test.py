import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.i5ype.mongodb.net/mongodb_test.py?retryWrites=true&w=majority"
client = MongoClient("mongodb+srv://admin:admin@cluster0.i5ype.mongodb.net/mongodb_test.py?retryWrites=true&w=majority")
db = client['pytech']
print(db.list_collection_names())