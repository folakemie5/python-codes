




import random
import time


o = [0,1,2,3,4,5,6,7,8,9]
code = ''.join([str(random.choice(o)) for i in range(10)])

univelcity_bank= {1234567890:{"Name": 'Seun Adeleye', "BVN": 2345432567, "Account_type": "Savings","Bal": 23400000, "ATM_pin": 2110, "Pin": 9898}, 3456789012:{"Name": 'Olanrewaju Dorcas', "BVN": 5678432467, "Account_type": "Savings","Bal": 123400000, "ATM_pin": 3310, "Pin": 3456}, 9021345678:{"Name": 'Eleanora Olanrewaju', "BVN": 1234567890, "Account_type": "Current","Bal": 1000000, "ATM_pin": 8575, "Pin": 1234}}
account=univelcity_bank.keys()

print("Welcome to Univelcity Bank PLC. Please enter your details as requested below to create an account with us.")
question=input("Would you like to continue: Yes/ No\n\t>")
if question.lower()=="yes":
    account_number=code
    name=input("Enter your name here\n\t>")
    bvn=int(input("Enter your 10-digit BVN\n\t>"))
    account_type=input("What is your account type: 'Current' or 'Savings'\n\t>")
    bal=int(input("How much do you want to deposit?\n\t>"))
    print("We know you may request for an atm in future. so, enter the details below")
    time.sleep(2)
    atm_pin=int(input("Enter your new and secured 4-digit ATM pin\n\t>"))
    pin=int(input("Enter your 4-digit USSD code\n\t>"))
    print(f"Your account number is {account_number}")
    univelcity_bank[account_number]= {"Name": name, "BVN": bvn, "Account_type": account_type,"Bal": bal, "ATM_pin": atm_pin, "Pin": pin}     

else:
    print("Goodbye.......")
    



transaction={}
print("What would you like to do today? Type 'W' for withdrawal and 'T' for transfer")
answer=input(">")
if answer.lower()=="w":
    transaction_type="Debit"
    your_pin=int(input("Enter your 4-digit ATM pin\n\t>"))
    if your_pin==atm_pin:
        amount=int(input("How much would you like to withdraw?\n\t>"))
        if amount<=bal:
            bal-=amount
            print("You have withdrawn {} naira. Your new balance is {}".format(amount,bal))
        else:
            print("The amount you want to withdraw is higher than your balance, enter new amount please.")
    else:
        print("Enter correct pin")
else:
    transaction_type="Debit"
    your_pin=int(input('Enter your 4-digit USSD pin\n\t>'))
    if your_pin==pin:
        recipient=int(input("Enter the account number of the recipient\n\t>"))
        if recipient in account:
            amount=int(input("How much do you want to transfer?\n\t>"))
            if amount<=bal:
                bal-=amount
                univelcity_bank[recipient]['Bal']+=amount
                print("You have transferred {} naira to {}. Your new balance is {}".format(amount,univelcity_bank[recipient]['Name'],bal))
                transaction[recipient]={"Amount": amount, "Trnsc_type": "Credit", "Bal": univelcity_bank[recipient]['Bal'] }
            else:
                print("The amount you want to transfer is higher than your balance, enter new amount please.")
        else:
            print("Please enter a valid account number")   
    else:
        print("Enter correct pin")        




transaction[account_number]={"Amount": amount, "Trnsc_type": transaction_type, "Bal": univelcity_bank[account_number]['Bal'] }

print(univelcity_bank)
print(transaction)





or


