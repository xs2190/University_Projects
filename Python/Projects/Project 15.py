# Shelby Jordan
# Project 15 
# Created: 3/28/2017
# This program will read numbers from a file, convert them to lettergrades
# and write the result to another file.
# ***********************************************************************
# ***********************************************************************

def main():
        # Open the lettergrades.txt file and read the strings.
        readFile = open('grades.txt', 'r')

        # Open the file that will be written to later.
        conversionFile = open('lettergrades.txt', 'w')
        
        # Counters for each possible lettergrade.
        countA = 0

        countB = 0

        countC = 0

        countD = 0

        countF = 0

        # While the grades.txt file has values, continue processing.
        for value in readFile:

                # convert the strings to integers.
                amount = int(value)

                # If the grade is greater than or equal to 90,
                # countA is incremented by 1.
                if amount >= 90:
                        
                        countA = countA + 1
                        
                # If the grade is greater than or equal to 80,
                # countB is incremented by 1. 
                elif amount >= 80:
                        
                        countB = countB + 1
                        
                # If the grade is greater than or equal to 70,
                # countC is incremented by 1. 
                elif amount >= 70:
                        countC = countC + 1
                        
                # If the grade is greater than or equal to 60,
                # countD is incremented by 1.         
                elif amount >= 60:
                        countD = countD + 1

                # If the grade is less than 60, increment countF
                # by 1.
                else:
                        countF = countF + 1

        # Write the counters for each lettergrade to the lettergrades.txt
        # file.
        conversionFile.write(str(countA) + ' of the grades are A(s)' + '\n')

        conversionFile.write(str(countB) + ' of the grades are B(s)' + '\n')

        conversionFile.write(str(countC) + ' of the grades are C(s)' + '\n')

        conversionFile.write(str(countD) + ' of the grades are D(s)' + '\n')

        conversionFile.write(str(countF) + ' of the grades are F(s)' + '\n')

        # Close the files.
        readFile.close

        conversionFile.close

# Call the main function
main()
