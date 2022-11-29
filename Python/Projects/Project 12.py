# Shelby Jordan
# Project 12 - Functions
# Created: 3/5/2017
# This program will calculate the factorial of an inputed integer
# ***********************************************************************
# ***********************************************************************

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
    number = int(input(' Please enter a number '))

    # Conditions for input greater than 0
    if number > 0:

        # Variable for factoral placeholder
        factorial = 1

        # Input of 0 calculations
        if number == 0:
            
            # Input of 0 output
            print ( 'The factorial of your input is' ,factorial)

            # Call on restart function
            restart()
            
        else:
            
            # While loop for calculating factoral
            while number > 0:

                # Factoral calculation
                factorial = number * factorial

                # Subtract 1 from input
                number = number - 1
                
            # Outout for an input > 0
            print ( 'The factorial of your input is' ,factorial)

            # Call the restart function
            restart()
    else:
        
        # Invalid entry response w/ restart option
        print ('No factorials for entry')
        
        # Call the restart function
        restart()
        
# Main function called
main()
    
