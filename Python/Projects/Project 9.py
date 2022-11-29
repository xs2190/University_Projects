# Shelby Jordan
# Project 9 - Repetition Structure
# Created: 3/5/2017
# This program will take integer input from the user and calculate
# the number of integers entered, how many were positive, and how many
# were negative and display the result.
# ***********************************************************************
# ***********************************************************************

# Delare variable, user must enter 0 to end
count = 1

countNeg = 0

countPos = 0

# Statement clarifying instructions
print ('If  "0" is entered then the program will end')

# Declare input from user
number = int(input('Please enter an integer. '))

# While loop for counting the numbers entered, the highest
# and lowest values as well
while number != 0:
    
    if number > 0:
        
        countPos = countPos + 1
        
        count = count + 1
        
        number = int(input('Please enter another integer '))
        
    else:
        
        count = count + 1
        
        countNeg = countNeg + 1
        
        number = int(input('Please enter another integer '))
        
# Output for each corresponding imput calculation
print (count, 'numbers were entered')

print (countNeg, 'numbers less than zero were entered')

print (countPos, 'numbers greater than zero were entered')

