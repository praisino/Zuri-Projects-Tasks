# Budget App
# Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for
# 1.  Depositing funds to each of the categories
# 2.  Withdrawing funds from each category
# 3.  Computing category balances
# 4.  Transferring balance amounts between categories

# IMPORTS
from datetime import datetime
from random import randint

# Store current date to now
now = datetime.now()

class budget:
    def __init__(budget, owner, balance, food, clothing, entertainment):
        budget.owner = owner
        budget.balance = balance
        budget.food = food
        budget.clothing = clothing
        budget.entertainment = entertainment

# DATABASE & FUNCTIONS
# Sample Users

database_user = {
   'Seyi':[3215406,'passwordSeyi'],
   'Mike':[5069858,'passwordMike'],
   'Love':[9392844,'passwordLove']
}
database_user["Seyi"].append(budget("Seyi", 3000, 200, 100, 30))
database_user["Mike"].append(budget("Mike", 1000, 500, 100, 100))
database_user["Love"].append(budget("Love", 2000, 200, 500, 500))

# Function for login
def login():
    
    name = input("What is your name? \n")
    password = input("Your password? \n")
    if(name in database_user and password == database_user[name][1]):
        print("\n ********* Welcome " + name + " *********")
        return True, name
    
    else:
        print("Password or Username Incorrect. Please try again")
        return False

# Function for Registeration
def register():
    # Register function
    name = input("What is your name? \n")
    password = input("Your new password? \n")
    default_val = 0
    
    if(name in database_user):
        print(name + " has been registered in the database, Pls choose another name or Login")
    else:
        accountNumber = randint(1000000, 9999999)
        database_user[name] = [accountNumber, password, budget(name, 0, 0, 0, 0 )]
        print("\n ********* Welcome " + name + " *********")
        print("Your account details are: \n Account Name:   " + name + "\n Account Number:", accountNumber)
        print("Thank you for using our services " + name + ". \n \n Please Login! \n")

# Function for bank Operation
def manageBudget():
    print("Today is:", now)
    print("Your current budget details are:")
    print("--------"*4)
    print("Budget balance: $", database_user[name][2].balance)
    print("- - - - "*3)
    print("Food Budget: $", database_user[name][2].food)
    print("Clothing Budget: $", database_user[name][2].clothing)
    print("Entertainment Budget: $", database_user[name][2].entertainment)
    print("--------"*4)
    print("--------"*4)
    print('Account Menu: These are the available options:')
    print('1. Cash Deposit')
    print('2. Withdrawal')
    print('3. Transfer')
    print('5. Exit')

    selectedOption = int(input('\n Please select an option:\n'))
    if(selectedOption == 1):
        print("NB: You can only deposit in your budget Balance.")
        depositAmount = int(input("Please, enter the amount you'd like to deposit: \n$"))
        database_user[name][2].balance = database_user[name][2].balance + depositAmount
        manageBudget()

    elif(selectedOption == 2):
        print("Where would you like to withdraw from?")
        print('1. Budget Balance')
        print('2. Food Budget')
        print('3. Clothing Budget')
        print('4. Entertainment Budget')
        print('5. Go back to the Account Menu')
        select = int(input("Select an option: "))
        withdrawAmount = int(input("How much would you like to withdraw"))

        if select == 1:
            database_user[name][2].balance = database_user[name][2].balance - withdrawAmount
            print("Your current Budget Balance is: $", database_user[name][2].balance)
        elif select == 2:
            database_user[name][2].food = database_user[name][2].food - withdrawAmount
            print("Your current Food Budget Balance is: $", database_user[name][2].food)
        elif select == 3:
            database_user[name][2].clothing = database_user[name][2].clothing - withdrawAmount
            print("Your current Clothing Budget Balance is: $", database_user[name][2].clothing)
        elif select == 4:
            database_user[name][2].entertainment = database_user[name][2].entertainment - withdrawAmount
            print("Your current Entertainment Budget Balance is: $", database_user[name][2].entertainment)
        elif select == 5:
            manageBudget()
        else:
            print("Invalid Selection, Please Try Again!")
        manageBudget()
    
    elif(selectedOption == 3):
        print("Please select the two budgets categories you'd like to transfer your funds from and to:")
        print("1. balance, 2. food, 3. clothing, 4. entertainment" )   
        transferDic = {
            "1":"balance",
            "2":"food",
            "3":"clothing",
            "4":'entertainment'
        }
        option1 = transferDic[input("From: ")]
        option2 = transferDic[input("To: ")]
        print("You'd be transferring from Budget", transferDic[option1], "to", transferDic[option2], "budget balance")
        amount = int(input("How much would you like to transfer? \n $"))
        
        amount1 = getattr(database_user[name][2], option['1'])
        setattr(database_user[name][2], option['1'], amount1 - amount)
        
        amount2 = getattr(database_user[name][2], option['2'])
        setattr(database_user[name][2], option['2'], amount2 + amount)
        manageBudget()
    
    elif selectedOption == 4:
        complaint = int(input('What issue will you like to report? \n'))
        print('Your message has being received. Thank you for contacting us!')
        manageBudget()

    elif(selectedOption == 5):
        exit()
    else:
        print('Invalid Option selected, please try again')


# FRONT END

#  Conditions
quit = False
while quit == False:

    print("Welcome, what would you like to do?")
    print("1. Login")
    print("2. Register")
    print("3. Quit")

    actionSelect = int(input("Select an option \n"))
        
    while True:
        if(actionSelect == 1):
            status, name = login()
            if status == True:
                manageBudget()
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
