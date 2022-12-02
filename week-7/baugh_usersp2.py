"""
Title: baugh_usersp2.py
Author: Ace Baugh
Date: 12/2/22
Description: Exercise 7.3 - Python with MongoDB Part II
"""

# import statements
from pymongo import MongoClient
import datetime

# connect to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@buwebdev-cluster-1.9wmv0d7.mongodb.net/web335DBretryWrites=true&w=majority")

print(client)
print("connected to MongoDB")

# store web335 database
db = client['web335DB']

# Create new user document
hayden = {
   'firstName': 'Joseph',
   'lastName': 'Hayden',
   'employeeId': '1014',
   'email': 'jhayden@gmail.com',
   'dateCreated': datetime.datetime.utcnow()
}

# Add new user document to database
hayden_user_id = db.users.insert_one(hayden).inserted_id

# Show user document
print("User added to MongoDB:")
print(db.users.find_one({'_id': hayden_user_id}))

# Update email of user document
db.users.update_one({'_id': hayden_user_id}, {'$set': {'email': 'jhayden@me.com'}})

# Show Updated user document
print(db.users.find_one({'_id': hayden_user_id}))

# Delete user document
db.users.delete_one({'_id': hayden_user_id})

# Show deleted user document
print(db.users.find_one({'_id': hayden_user_id}))
