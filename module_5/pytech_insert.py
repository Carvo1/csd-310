""" 
    Title: pytech_insert.py
    Author: Steffan Hinkle
    Date: 20 June 2021
    Description: Test program for inserting new documents 
                 into the students collection 
"""

#Importing Required modules
from pymongo import MongoClient

#Creating variable containing the MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.xfhf4.mongodb.net/pytech?retryWrites=true&w=majority"

#Creating variable to connect to MongoDB cluster
client = MongoClient(url)

#Creating variable to for connecting to the Pytech database
db = client.pytech


#Creating variable for doe with student information
doe = {
      "student_id": "1007",
      "first_name": "John",
      "last_name": "Doe",
      "enrollments": [
        {
          "term": "Session 1",
          "gpa": "4.0",
          "start_date": "1/1/2021",
          "end_date": "3/31/2021",
          "courses": [
            {
              "course_id": "100",
              "desciption": "Python Crash Course",
              "instructor": "Mrs Brown",
              "grade": "A+"
            },
            {
              "course_id": "101",
              "desciption": "Introduction to Databases",
              "instructor": "Mr Blue",
              "grade": "A+"
            }
            ]
        },
        {
          "term": "Session 2",
          "gpa": "4.0",
          "start_date": "4/1/2021",
          "end_date": "6/30/2021",
          "courses": [
            {
              "course_id": "102",
              "desciption": "Python For Data Science",
              "instructor": "Mrs Brown",
              "grade": "A+"
            },
            {
              "course_id": "103",
              "desciption": "Databases in Web Applications",
              "instructor": "Mr Blue",
              "grade": "A+"
            }
            ]
        }
        ]
}
#Creating variable for turner with student information
turner = {
      "student_id": "1008",
      "first_name": "Sam",
      "last_name": "Turner",
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
              "grade": "B"
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
              "grade": "B"
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
#Creating variable for thomas with student information
thomas = {
      "student_id": "1009",
      "first_name": "Mike",
      "last_name": "Thomas",
      "enrollments": [
        {
          "term": "Session 1",
          "gpa": "3.0",
          "start_date": "1/1/2021",
          "end_date": "3/31/2021",
          "courses": [
            {
              "course_id": "100",
              "desciption": "Python Crash Course",
              "instructor": "Mrs Brown",
              "grade": "C+"
            },
            {
              "course_id": "101",
              "desciption": "Introduction to Databases",
              "instructor": "Mr Blue",
              "grade": "C+"
            }
            ]
        },
        {
          "term": "Session 2",
          "gpa": "3.0",
          "start_date": "4/1/2021",
          "end_date": "6/30/2021",
          "courses": [
            {
              "course_id": "102",
              "desciption": "Python For Data Science",
              "instructor": "Mrs Brown",
              "grade": "B"
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

#Creating variable for the students collections
students = db.students


print("\n -- INSERT STATEMENTS --")

#Insert statement with output for John Doe
doe_student_id = students.insert_one(doe).inserted_id
print(" Inserted student record John Doe into the students collection with document_id " + str(doe_student_id))

#Insert statement with output for Sam Turner
turner_student_id = students.insert_one(turner).inserted_id
print(" Inserted student record Sam Turner into the students collection with document_id " + str(turner_student_id))

#Insert statement with output for Mike Thomas
thomas_student_id = students.insert_one(thomas).inserted_id
print(" Inserted student record Mike Thomas into the students collection with document_id " + str(thomas_student_id))

#Final statement informing user the program has finished
input("\n\n End of program, press any ket to exit... ")