""" 
    Title: mongodb_test.py
    Author: Steffan Hinkle
    Date: 20 June 2021
    Description: Test program for connecting to a 
                 MongoDB Atlas cluster
"""

#Importing Required modules
from pymongo import MongoClient

#Creating variable containing the MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.xfhf4.mongodb.net/pytech?retryWrites=true&w=majority"

#Creating variable to connect to MongoDB cluster
client = MongoClient(url)

#Creating variable to for connecting to the Pytech database
db = client.pytech

#Printing the selected collections from the database and then exiting 
print("\n -- Pytech COllection List -- ")
print(db.list_collection_names())
input("\n   End of program, press any key to exit...")