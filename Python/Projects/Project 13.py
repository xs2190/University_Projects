# Shelby Jordan
# Project 13 Functions
# Created: 3/5/2017
# This program will calculate the highest/lowest numbers entered
# and display the results using functions
# ***********************************************************************
# ***********************************************************************

# Statement clarifying instructions
print ('If  "0" is entered then the program will restart')

# Function to restart the main function
def restart():

    # User input for restart option
    restart = input("Would you like to restart this program? y/n ")

    # Conditions for restarting main function
    if restart == "y":

        # Call on main function
        main()
        
    else:

        # Response for anything other than yes
        print ("Script terminating. Goodbye.")

# Defining main function
def main():

    # User input
    number = int(input('Please enter a number '))

    # Variable for the highest value input
    maxnumber = number

    # Variable for the lowest value input
    minnumber = number

    # While loop that will run as long as input is not 0
    while number != 0:

        # Change max number if condition is met
        if number > maxnumber:
            maxnumber = number

        # Change min number if condition is met    
        elif number < minnumber:
            minnumber = number
    
        number = int(input('Please enter another number '))

    # print results of calculation
    print ('The largest number entered was', maxnumber)

    print ('The smallest number entered was', minnumber)
    
    # call on restart function
    restart()
    
# call on main function
main()


    


    
