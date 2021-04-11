# imports
from datetime import datetime #To show current Date

now = datetime.now()
# Database
name = input("What is your name? \n")
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['passwordSeyi','passwordMike','passwordLove']

# Login phase
if(name in allowedUsers):
    password = input("Your Paassword? \n")
    userid = allowedUsers.index(name)

    if(password == allowedPassword[userid]):
        # Account Options
        print(now)
        print('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option: \n'))

        # Account Options output
        if(selectedOption == 1):
            withdrawAmount = int(input('How much would you like to withdraw? \n'))
            print('Take your cash: $' + str(withdrawAmount))

        elif(selectedOption == 2):
            depositAmount = int(input('How much would you like to deposit? \n'))
            print('Your current balance ', now,' is: $' + str(depositAmount))
            
        elif(selectedOption == 3):
            complaint = int(input('What issue will you like to report? \n'))
            print('Your message has being received. Thank you for contacting us!')
        else:
            print('Invalid Option selected, please try again')

    else:
        print('Password Incorrect, please try again') 
else:
    print('Name not found, please try again')