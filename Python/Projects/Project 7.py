# Shelby Jordan
# Project 7 - The Repetition Structure
# Created: 2/28/2017
# This program will print the even numbers between 1 and 100
# ***********************************************************************
# ***********************************************************************

# Declare variables
count = 1

for count in range (1, 101, 1): # loop incremented by 1 using FOR and RANGE
    if count <= 100 and count % 2 == 0: # is count less than 100 and even?
        print (count) # print even number
        count = count + 1 # add one to it
    else: # add 1 to count regardless if it met conditions above
        count = count + 1
    
