# Shelby Jordan
# Project 8 - Repetition Structure
# Created: 3/5/2017
# This program will calculate the factorial of an inputed integer
# ***********************************************************************
# ***********************************************************************

# Ask for user input
# Delcare variable
number = int(input(' Please enter a number '))

# Loop for calculating factorials with print statement
if number > 0:
    factorial = 1
    if number == 0:
        print (factorial)
    else:
        while number > 0:
            factorial = number * factorial
            number = number - 1
        print ( 'That factorial is', factorial)
else:
    print ('No factorials for entry')


    
