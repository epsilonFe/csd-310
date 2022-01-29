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

student_list = students.find({})
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"]+"\n")
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Burbank"}})

result = students.find_one({"student_id": "1007"})

print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")
print("Student ID: " + result["student_id"] + "\nFirst Name: " + result["first_name"] + "\nLast Name: " + result["last_name"]+"\n")