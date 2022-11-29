dictRoom = {'CS101':'3004', 'CS102':'4501', 'CS103':'6755', 'NT110':'1244',
            'CM241':'1411'}

dictInstructor = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich',
                  'NT110':'Burke','CM241':'Lee'}

dictMeetingTime = {'CS101':'8:00 a.m.', 'CS102':'9:00 a.m.',
                   'CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'}

def restart():

    restart = input('Restart this program? y/n ')

    if restart == 'y':

        main()

    else:

        print('Goodbye')

def check(userInput):

    if userInput in dictRoom:

        return 'True'

def main():
    
    print('Acceptable entries are CS101, CS102, CS103, NT110, or CM241.')

    userInput = input('Enter the course number you wish to get information about: ' )
    
    userInput = userInput.upper()

    if check(userInput) == 'True':

        print('The requested course information is as follows.')
        print('Room number:',dictRoom[userInput])
        print('Instructor:', dictInstructor[userInput])
        print('Meeting Time:', '[',dictMeetingTime[userInput],']')
        restart()

    else:
        print('Invalid entry')
        restart()


main()


    



