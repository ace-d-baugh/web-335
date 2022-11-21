"""
Title: baugh_hobbies.py
Author: Ace Baugh
Date: 11/21/22
Description: Exercise 6.3 - Python with MongoDB Part I
"""

# import statements
from pymongo import MongoClient

# connect to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@buwebdev-cluster-1.9wmv0d7.mongodb.net/web335DBretryWrites=true&w=majority")

print (client)
print ("connected to MongoDB")

# store web335 database
db = client['web335DB']

# Display the web335DB user's collection
print ("web335DB users collection: ")
# loop through the collection and print each document
for user in db.users.find():
   print (user)

# Display the web335DB employeeId 1011 document
print ("web335DB employeeId 1011 document: ")
print (db.users.find_one({"employeeId": "1011"}))

# Display the web335DB lastName Mozart document
print ("web335DB lastName Mozart document: ")
print (db.users.find_one({"lastName": "Mozart"}))