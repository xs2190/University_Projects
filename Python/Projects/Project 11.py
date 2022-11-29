# Shelby Jordan
# Project 11 - Currency Converter
# Created: 3/5/2017
# This program will convert dollars into Pesos
# ***********************************************************************
# ***********************************************************************

# Function to restart the main function
def restart():

    # User input for restart option
    restart = input("Would you like to restart this program? y/n ")

    # Conditions for restarting main function
    if restart == "y":
        
        main()
        
    else:
        
        print ("Script terminating. Goodbye.")

# Defining main function
def main():
    
    # User input
    amount1 = int(input('Enter the US Dollar amount you wish to convert into Pesos '))

    # Calculation
    pesos = amount1 * 19.52

    # Display results
    print ( amount1," dollars is equivalent to", pesos,"Pesos as of 3/5/2017")
    
    # Call on restart function
    restart()

# Main function called
main()
