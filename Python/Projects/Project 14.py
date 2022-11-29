# Shelby Jordan
# Project 14 
# Created: 3/27/2017
# This program will read the highest/lowest numbers from a file
# and display the results
# ***********************************************************************
# ***********************************************************************

def main():
    # Open the numbers.txt file and read the strings
    read_file = open('numbers.txt', 'r')

    # Set the smallest number and the largest number equal
    # to zero.
    maxnumber = 0
        
    minnumber = 0

    # While the file has a value in a line, continue processing.
    for value in read_file:

        # Convert each value into an integer
        amount = int(value)

        # Change the value of the maxnumber to the new
        # amount if amount is larger than the current max
        if amount > maxnumber:
        
            maxnumber = amount

        # If amount is not greater than the max and it is
        # less than the min, set minnumber to the new lowest
        # number
        elif amount < minnumber:
        
            minnumber = amount

    # Display the largest number and the smallest number
    # in the text file.
    print ('The largest number was', maxnumber)
    print ('The smallest number was', minnumber)

    # close the file
    read_file.close

main()


