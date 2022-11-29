# Shelby Jordan
# Project 18
# The program will calculate the sum of a series of unspaced numbers and
# display the results.
# ************************************************************************
# ************************************************************************
# ************************************************************************

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
        print ("Script terminating.....goodbye.")

def main():
    # Sum variable
    summation = 0

    # Intstuctions for user
    print('Please enter a series of single-digit numbers with nothing seperating'
              ' them', ':', sep= ' ', end= ' ')

    # User input
    numbersInput = input()

    # If the input is a number, continue processing
    if numbersInput.isdigit:

        # Seperate the input into different elements in a list
        value = [g.split()[0] for g in numbersInput]

        # Converts each item in the list into an integer then
        # adds them together
        for j in value:

            conversion = int(j)

            summation = conversion + summation

        # Print the sum and call restart function
        print('The total of your entry is: ', summation)
        restart()

    # Anything other than numbers will call the restart function
    else:
        print('Invalid entry')
        restart()

main()
