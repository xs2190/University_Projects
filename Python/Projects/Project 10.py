# Shelby Jordan
# Project 10 Repetition Structures
# Created: 3/5/2017
# This program will calculate the highest/lowest numbers entered
# and display the results
# ***********************************************************************
# ***********************************************************************

# Statement clarifying instructions
print ('If  "0" is entered then the program will end')

# Declare variables
number = int(input('Please enter a number '))

maxnumber = number

minnumber = number

# While loop for calculating the max/min numbers
while number != 0:
    
    if number > maxnumber:
        maxnumber = number
        
    elif number < minnumber:
        minnumber = number
        
    number = int(input('Please enter another number '))

# Output for each corresponding imput calculation
print ('The largest number entered was', maxnumber)
print ('The smallest number entered was', minnumber)



    


    
