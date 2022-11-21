/**
	Title: baugh-aggregate-queries.js
   Author: Ace Baugh
   house.js written by Professor Krasso
   Date: 21 November 2022
   Description: Code snippets for: Manipulating  the houses and students collections.
                  As well as querying the students collection using aggregate queries.
 */

// Show a list of documents in the houses collection (#2)
db.houses.find({});

// Show a list of documents in the students collection (#3)
db.students.find({});

// Add a document to the students collection (#4.1)
db.students.insertOne({firstName: 'Ace', lastName: 'Baugh', studentId: 's1069', houseId: 'h1009'})

// Verify the document was added to the students collection (#4.2)
db.students.findOne({lastName: 'Baugh'});

// Delete the recently added document from the students collection (#5.1)
db.students.deleteOne({lastName: 'Baugh'});

// Verify the document was deleted from the students collection (#5.2)
db.students.findOne({lastName: 'Baugh'});

// Show all students by house name using $lookup (#6)
db.students.aggregate({ $lookup: {
                        from: 'houses', 
                        localField: 'houseId', 
                        foreignField: 'houseId', 
                        as: 'house'} 
                     });

// Show all students of Gryffindor house using $lookup and $match (#7)
db.students.aggregate({ $lookup: {
                        from: 'houses', 
                        localField: 'houseId', 
                        foreignField: 'houseId', 
                        as: 'house'} 
                     }, { 
                        $match: { 'house.houseId': 'h1007' } 
                     });

// Show all students with Eagle mascot using $lookup and $match (#8)
db.students.aggregate({ $lookup: {
                        from: 'houses', 
                        localField: 'houseId', 
                        foreignField: 'houseId', 
                        as: 'house'} 
                     }, { 
                        $match: { 'house.mascot': 'Eagle' } 
                     });