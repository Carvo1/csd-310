"""
    Title: pytech_delete.py
    Author: Steffan Hinkle
    Date: 27 June 2021
    Description: Test program to insert and then delete a document in the pytech collection
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



#Creating variable for george with student information
george = {
      "student_id": "1010",
      "first_name": "George",
      "last_name": "Chambers",
      "enrollments": [
        {
          "term": "Session 1",
          "gpa": "3.5",
          "start_date": "1/1/2021",
          "end_date": "3/31/2021",
          "courses": [
            {
              "course_id": "100",
              "desciption": "Python Crash Course",
              "instructor": "Mrs Brown",
              "grade": "B"
            },
            {
              "course_id": "101",
              "desciption": "Introduction to Databases",
              "instructor": "Mr Blue",
              "grade": "B+"
            }
            ]
        },
        {
          "term": "Session 2",
          "gpa": "3.5",
          "start_date": "4/1/2021",
          "end_date": "6/30/2021",
          "courses": [
            {
              "course_id": "102",
              "desciption": "Python For Data Science",
              "instructor": "Mrs Brown",
              "grade": "B+"
            },
            {
              "course_id": "103",
              "desciption": "Databases in Web Applications",
              "instructor": "Mr Blue",
              "grade": "B"
            }
            ]
        }
        ]
}

#Printing data for student george
print("\n -- INSERT STATEMENTS --")

#Insert statement with output for George Chambers
george_student_id = students.insert_one(george).inserted_id
print(" Inserted student record into the students collection with document_id " + str(george_student_id))

#Creating variable which holds a single students information
georgeinfo = students.find_one({"student_id" : "1010"})

#Printing the single selected students information to the user in the same format as the iterated students above
print("\n -- DISPLAYING STUDENT TEST DOC --")
print("Student_ID: " + georgeinfo["student_id"] + "\nFirst Name: " + georgeinfo["first_name"] + "\nLast Name: " + georgeinfo["last_name"] + "\n")

#Deleting the recently added student 1010 from the collection
students.delete_one({"student_id" : "1010"})



#Variable storing the results of querying all the students
list_of_students = students.find({})

#Printing the students and their data for the user
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#Using a for look to iterate through all the student data displaying the results one student at a time
for student in list_of_students:
    print("Student_ID: " + student["student_id"] + "\nFirst Name: " + student["first_name"] + "\nLast Name: " + student["last_name"] + "\n")

#Final statement informing user the program has finished
input("\nEnd of program, press any ket to exit... ")