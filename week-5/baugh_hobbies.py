"""
Title: baugh_hobbies.py
Author: Ace Baugh
Date: 11/16/22
Description: Exercise 5.3 - Python Conditionals, Lists, and Loops
"""

# List of hobbies
hobbies = ["photography", "origami", "cooking", "camping", "park hopping", "crocheting"]

# function to choose a random hobby
def choose_hobby():
   import random
   return random.choice(hobbies)

# for loop to print each hobby
for hobby in hobbies:
   print(hobby)

# days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# for loop to print each day
for day in days:
   # if statement to print if day is a weekend: Saturday or Sunday is a time for hobby or print it is a work day
   if day == "Saturday" or day == "Sunday":
      # concatenate string with hobby
      print(day + " is a day off: I am free to enjoy " + choose_hobby() + ".")
   else:
      # concatenate string with hobby
      print(day + " is a work day: I am busy with work. No time for " + choose_hobby() + ".")