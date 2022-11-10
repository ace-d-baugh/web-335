/**
	Title: baugh_MongoDB_Shell.js
   Author: Ace Baugh
   Date: 09 November 2022
   Description: MongoDB Shell Scripts for the users collection.
 */ 

   // Connection String
// mongosh "mongodb+srv://buwebdev-cluster-1.9wmv0d7.mongodb.net/web335DB" --apiVersion 1 --username web335_user

//Loads the users file
load('users.js');

// Query to find users
db.users.find({});

// Query to find users by email
db.users.find({ email: 'jbach@me.com' });

// Query to find users by last name
db.users.find({ lastName: 'Mozart' });

// Query to find users by first Name
db.users.find({ firstName: 'Richard' });

// Query to find users by employeeId
db.users.find({ employeeId: '1010' });
