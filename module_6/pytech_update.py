"""
    Title: pytech_update.py
    Author: Steffan Hinkle
    Date: 27 June 2021
    Description: Test program to update a document in the pytech collection
"""

#Importing Required modules
from pymongo import MongoClient

#Creating variable containing the MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.xfhf4.mongodb.net/pytech?retryWrites=true&w=majority"

#Creating variable to connect to MongoDB cluster
client = MongoClient(url)

#Creating variable to for connecting to the Pytech database
db = client.pytech

#Creating variable for the students collections
students = db.students



#Variable storing the results of querying all the students
list_of_students = students.find({})

#Printing the students and their data for the user
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#Using a for look to iterate through all the student data displaying the results one student at a time
for student in list_of_students:
    print("Student_ID: " + student["student_id"] + "\nFirst Name: " + student["first_name"] + "\nLast Name: " + student["last_name"] + "\n")



#Using update_one to select a specific student and update their last name, the reset statement is commented out below
students.update_one({"student_id":"1007"},{"$set":{"last_name":"Jacobs"}})
#students.update_one({"student_id":"1007"},{"$set":{"last_name":"Doe"}})

#Creating variable which holds a single students information
john = students.find_one({"student_id" : "1007"})

#Printing the single selected students information to the user in the same format as the iterated students above
print("\n -- DISPLAYING STUDENT DOCUMENT 1007 --")
print("Student_ID: " + john["student_id"] + "\nFirst Name: " + john["first_name"] + "\nLast Name: " + john["last_name"] + "\n")

#Final statement informing user the program has finished
input("\nEnd of program, press any ket to exit... ")