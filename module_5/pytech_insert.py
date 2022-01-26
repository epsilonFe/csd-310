import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.i5ype.mongodb.net/pytech?retryWrites=true&w=majority")
db = client["pytech"]
students = db["students"]
students.delete_many({})
fred = {
    "first_name": "Fred",
    "student_id":"1007"
}
students.insert_one(fred)

brad = {
    "first_name": "Brad",
    "student_id":"1008"
}
students.insert_one(brad)

frank = {
    "first_name": "Frank",
    "student_id":"1009"
}
students.insert_one(frank)

docs = db.students.find({})
for doc in docs:
    print(doc)