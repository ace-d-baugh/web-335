/**
	Title: baugh-projections.js.js
   Author: Ace Baugh
   Date: 16 November 2022
   Description: Code snippets for: Adding user, updating a user's email, 
   seeing that change and using project to filter the user query.
 */

// Connection String
// mongosh "mongodb+srv://buwebdev-cluster-1.9wmv0d7.mongodb.net/web335DB" --apiVersion 1 --username web335_user

// add new user to the users collection
db.users.insertOne({
      "firstName": "Ace",
      "lastName": "Baugh",
      "employeeId": "1013",
      "email": "ace.d.baugh@gmail.com",
      "dateCreated": new Date(),
});

// update the user's email address
db.users.updateOne({
      "lastName": "Mozart",
}, { $set: { "email": "mozart@me.com" } });

// view updated user
db.users.aggregate({ $match: { "lastName": "Mozart" } });

// list all users with project clause for first and last names and email
db.users.aggregate({ $project: { "_id": 0, "firstName": 1, "lastName": 1, "email": 1 } } );