

# Open the lettergrades.txt file and read the strings
read_file = open('grades.txt', 'r')
conversion_file = open('lettergrades.txt', 'w')


countA = 0
countB = 0
countC = 0
countD = 0
countF = 0

for value in read_file:

        amount = int(value)

        if amount >= 90:
                countA = countA + 1
        elif amount >= 80:
                countB = countB + 1
        elif amount >= 70:
                countC = countC + 1
        elif amount >= 60:
                countD = countD + 1
        else:
                countF = countF + 1


conversion_file.write(str(countA) + 'Are grade A' + '\n')
conversion_file.write(str(countB) + 'Are grade B' + '\n')
conversion_file.write(str(countC) + 'Are grade C' + '\n')
conversion_file.write(str(countD) + 'Are grade D' + '\n')
conversion_file.write(str(countF) + 'Are grade F' + '\n')

read_file.close
conversion_file.close
