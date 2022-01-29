import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.i5ype.mongodb.net/pytech?retryWrites=true&w=majority")
db = client["pytech"]
students = db["students"]
students.delete_many({})
fred = {
    "first_name": "Fred",
    "last_name": "Fisk",
    "student_id":"1007"
}
students.insert_one(fred)

brad = {
    "first_name": "Brad",
    "last_name": "Darby",
    "student_id":"1008"
}
students.insert_one(brad)

frank = {
    "first_name": "Frank",
    "last_name": "Sink",
    "student_id":"1009"
}
students.insert_one(frank)

docs = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENT FROM find() QUERY --")
for doc in docs:
    print("Student ID:", doc["student_id"])
    print("First Name:", doc["first_name"])
    print("Last Name:", doc["last_name"])
    print()
print("-- INSERT STATEMENTS --")
students.insert_one({"first_name":"John","last_name":"Doe","student_id":"1010"})
inserted=students.find_one({"student_id":"1010"})
print("Inserted student record into the students collection with document_id",inserted.get("_id"))
print()
print("-- DISPLAYING STUDENTS TEST DOC --")
print("Student ID:", inserted["student_id"])
print("First Name:", inserted["first_name"])
print("Last Name:", inserted["last_name"])
students.delete_one({"student_id":"1010"})
print()
docs = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENT FROM find() QUERY --")
for doc in docs:
    print("Student ID:", doc["student_id"])
    print("First Name:", doc["first_name"])
    print("Last Name:", doc["last_name"])
    print()