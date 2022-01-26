import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.i5ype.mongodb.net/pytech?retryWrites=true&w=majority")
db = client["pytech"]
students = db["students"]
docs = db.students.find({})
for doc in docs:
    print(doc)

print(students.find_one({"student_id":"1007"}))
