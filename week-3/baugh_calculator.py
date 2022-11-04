"""
Title: myworld.py
Author: Ace Baugh
Date: 11/2/22
Description: Exercise 3.3 - Python Variables and Functions
"""

# function to add two numbers
def add(add1, add2):
   return add1 + add2

# function to subtract two numbers
def subtract(subtract1, subtract2):
   return subtract1 - subtract2

# function to divide two numbers
def divide(divide1, divide2):
   return divide1 / divide2
   
# function to multiply two numbers
def multiply(multiply1, multiply2):
   return multiply1 * multiply2

#creating test variables
add1 = 4
add2 = 4
subtract1 = 10
subtract2 = 6
divide1 = 8
divide2 = 2
multiply1 = 10
multiply2 = 2

# creating an output variable to store the results of the functions
output = str(add1) + " + " + str(add2) + " is " + str(add(add1, add2)) + ".\n" + str(subtract1) + " - " + str(subtract2) + " is " + str(subtract(subtract1, subtract2)) + ".\n" + str(divide1) + " / " + str(divide2) + " is " + str(divide(divide1, divide2)) + ".\n" + str(multiply1) + " * " + str(multiply2) + " is " + str(multiply(multiply1, multiply2)) + "."

# printing the output variable
print(output)


