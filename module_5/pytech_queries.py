""" 
    Title: pytech_queries.py
    Author: Steffan Hinkle
    Date: 20 June 2021
    Description: Test program for querying the students collection.
"""

#Importing Required modules
from pymongo import MongoClient

#Creating variable containing the MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.xfhf4.mongodb.net/pytech?retryWrites=true&w=majority"

#Creating variable to connect to MongoDB cluster
client = MongoClient(url)

#Creating variable to for connecting to the Pytech database
db = client.pytech

#Creating students variable to represent all students in collection
students = db.students

#Variable storing the results of querying all the students
list_of_students = students.find({})

#Printing the students and their data for the user
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#Using a for look to iterate through all the student data displaying the results one student at a time
for student in list_of_students:
    print("Student_ID: " + student["student_id"] + "\nFirst Name: " + student["first_name"] + "\nLast Name: " + student["last_name"] + "\n")

#Creating variable which holds a single students information
turner = students.find_one({"student_id" : "1008"})

#Printing the single selected students information to the user in the same format as the iterated students above
print("\n -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("Student_ID: " + turner["student_id"] + "\nFirst Name: " + turner["first_name"] + "\nLast Name: " + turner["last_name"] + "\n")


#Final statement informing user the program has finished
input("\nEnd of program, press any ket to exit... ")
