# Puts all keys in a list
def keys(g):

    count = g

    if count < 50:
        for key in object1.dictStates:
            keyList[count] = key
            count += 1

# Puts all the values in a list
def values(g):

    count = g

    if count < 50:
        for value in capitals:
            valueList[count] = value
            count += 1

# Quiz the user
def quiz():

    import random
    randomCount = random.randint(0,49)

    print('What is the capital of',keyList[randomCount],'?')
    question = input()
    value = valueList[randomCount]
    response = question.lower()
    answer = value.lower()
    
    if response == answer:

        global numberCorrect
        numberCorrect += 1
        print('Correct')
        again()

    else:

        global numberWrong
        numberWrong += 1
        print('Incorrect')
        again()
    
# Ask the user to continue
def again():

    again = input('Would you like to continue? y/n ')

    if again == 'y':

        quiz()

    else:

        print('You answered', numberCorrect, 'correct and', numberWrong, 'incorrect.')
        print('Goodbye')


def main(i):

    count = i
    
    keys(count)
    
    values(count)
    
    quiz()




class states:
    # create a dictionary of states with capitols
    dictStates = {'Alabama':'Montgomery','Alaska':'Juneau', 'Arizona':'Phoenix',
                  'Arkansas':'Little Rock', 'California':'Sacramento', 'Colorado':'Denver',
                  'Connecticut':'Hartford', 'Delaware':'Dover','Florida':'Tallahassee',
                  'Georgia':'Atlanta', 'Hawaii':'Honolulu', 'Idaho':'Boise',
                  'Illinois':'Springfield','Indiana':'Indianapolis','Iowa':'Des Moines',
                  'Kansas':'Topeka','Kentucky':'Frankfort','Louisiana':'Baton Rouge',
                  'Maine':'Augusta','Maryland':'Annapolis', 'Massachusetts':'Boston',
                  'Michigan':'Lansing','Minnesota':'St. Paul','Mississippi':'Jackson',
                  'Missouri':'Jefferson City','Montana':'Helena','Nebraska':'Lincoln',
                  'Nevada':'Carson City','New Hampshire':'Concord','New Jersey':'Trenton',
                  'New Mexico':'Santa Fe','New York':'Albany','North Carolina':'Raleigh',
                  'North Dakota':'Bismarck','Ohio':'Columbus','Oklahoma':'Oklahoma City',
                  'Oregon':'Salem','Pennsylvania':'Harrisburg','Rhode Island':'Providence',
                  'South Carolina':'Columbia','South Dakota':'Pierre','Tennessee':'Nashville',
                  'Texas':'Austin','Utah':'Salt Lake City','Vermont':'Montpelier',
                  'Virginia':'Richmond','Washington':'Olympia','West Virginia':'Charleston',
                  'Wisconsin':'Madison','Wyoming':'Cheyenne'}

# Opening statement
print('This program will quiz your knowledge of state capitals.')

object1 = states()

#Creates a touple of all values
capitals = object1.dictStates.values()

#counters
count2 = 0

numberCorrect = 0

numberWrong = 0

#lists
keyList = [0] * 50

valueList = [0] * 50

#call main
main(count2)
    



