# IMPORTS
from datetime import datetime
from random import randint

# BACK END

# Store current date to now
now = datetime.now()

# DATABASE & FUNCTIONS
database_user = {
   'Seyi':[3215406,'passwordSeyi'],
   'Mike':[5069858,'passwordMike'],
   'Love':[9392844,'passwordLove']
}


# Function for login
def login():
    
    name = input("What is your name? \n")
    password = input("Your password? \n")
    if(name in database_user and password == database_user[name][1]):
        print("\n ********* Welcome " + name + " *********")
        print("Today is:", now)
        print("Your account details are: \n Account Name:   " + name + "\n Account Number:", database_user[name][0])
        return True
    else:
        print("Password or Username Incorrect. Please try again")
        return False

# Function for Registeration
def register():
    # Register function
    name = input("What is your name? \n")
    password = input("Your new password? \n")
    
    if(name in database_user):
        print(name + " has been registered in the database, Pls choose another name or Login")
    else:
        accountNumber = randint(1000000, 9999999)
        database_user[name] = [accountNumber, password]
        print("\n ********* Welcome " + name + " *********")
        print("Your account details are: \n Account Name:   " + name + "\n Account Number:", accountNumber)
        print("Thank you for using our services " + name + ". \n \n Please Login! \n")

# Function for bank Operation
def bankOperations():
    
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = int(input('\n Please select an option:'))
            
    if(selectedOption == 1):
        print('you selected %s' % selectedOption)
        withdrawAmount = int(input('How much would you like to withdraw? \n'))
        print('Take your cash: $' + str(withdrawAmount))
        bankOperations()
                
    elif(selectedOption == 2):
        print('you selected %s' % selectedOption)
        depositAmount = int(input('How much would you like to deposit? \n'))
        print('Your current balance ', now ,' is: $' + str(depositAmount))
        bankOperations()
                
    elif(selectedOption == 3):
        print('you selected %s' % selectedOption)
        complaint = int(input('What issue will you like to report? \n'))
        print('Your message has being received. Thank you for contacting us!')
        bankOperations()

    elif(selectedOption == 4):
        exit()
    else:
        print('Invalid Option selected, please try again')
    
# FRONT END

# Conditions
quit = False
while quit == False:

    print("Welcome, what would you like to do?")
    print("1. Login")
    print("2. Register")
    print("3. Quit")

    actionSelect = int(input("Select an option \n"))
        
    while True:
        if(actionSelect == 1):
            if login() == True:
                bankOperations()
            else:
                break
        elif(actionSelect == 2):
            register()
            break 

        elif(actionSelect == 3):
            exit()
        
        else:
            print("wrong Selection!, Please make a correct selection. Thanks!")
        actionSelect = ''
print("Thank you for banking with us!")