# users= {"eri1234": {"password": "1234", "has_note": False}, "seun456": {"password": "0000", "has_note": True}}
# def create_account(username):
#     name_of_notepad=("{}.txt".format(username))
#     notepad=open(name_of_notepad, "w")
#     content=notepad.write(input("Enter your content here\n>"))
#     y=open(name_of_notepad,"a")
#     more_content=y.writelines(input("\nEnter more content here\n\t>"))
#     users[username]['has_note']=True



# print("Hello. Welcome to Notepad.ng. Press'C' to continue and 'R' to register as a new user")

# response=input("Enter 'C' or 'R'\n>")
# if response.lower()=='c':
#     username=input("Enter your username\n>")
#     if username in users.keys():
#         my_password=input("Enter your password\n>")
#         if my_password == users[username]["password"]:
            
#             print("Welcome {}. Do you want to create a notepad? Enter 'Y' for Yes and 'N' for No".format(username))
#             answer=input("Enter 'Y' or 'N'\n>")
#             if answer.lower()=="y":
#                 if users[username]["has_note"]==False:
#                     print("Now you can write in your notepad")
#                     create_account(username)            
#                     print(users)
#                 else:
#                     print("You already have a notepad, Press 'M' to write more content or 'X' to cancel")
#                     reply=input("\n'M' or 'X'\n\t")
#                     if reply.lower()=="m":
#                         create_account(username)
#                         print(users)
#                     else:
#                         print("It was nice to see you again")  
#             else:
#                 print("Thanks for stopping by")
#         else:
#             print("Enter the correct password")
#     else:
#         print("Please enter correct username or register if you are a new user")
# else:
#     print("Welcome. Fill the details below")
#     username=input("Enter a new username\n\t>")
#     myPassword=input("Enter a password\n\t")
    

#     users[username]= {
#         'password': myPassword
#         }
#     users[username]['has_note']=False
#     print(users)
#     print("Welcome {}. Do you want to create a notepad? Enter 'Y' for Yes and 'N' for No".format(username))
#     answer=input("Enter 'Y' or 'N'\n>")
#     if answer.lower()=="y":
#         print("Now you can write in your notepad")
#         create_account(username)
#         # notepad=open("{}.txt".format(username), "w")
#         # content=notepad.writelines(input("Enter your content here\n>"))
#         # j=open("{}.txt".format(username), "r")
#         # users[username]['has_note']=True
       
#         print(users)
       
    


 






        


# or
##### NOTEPAD CORRECTION #######


users = {
    "eri1234": {"password": "1234", "has_note": False}, 
    "seun456": {"password": "0000", "has_note": True}
}

users_store=open("users.txt","w")
users_store.write(str(users))



def login(username, password):
    " Takes in the user name and password and checks it with the users dictionary. Returns true if user name and password is correct else it returns false."

    user = users.get(username)
    if user:
        if user['password'] == password:
            print("Login successful")
            return True
    
    return False


def signup(username, password):
    "Takes in the username and password and creates a user in the users dictionary"

    if username in users.keys():
        print(f"{username} already exists!")
        return False
    else:
        users[username] = {
            'password' : password,
            'has_note' : False
        }
        users_store=open("users.txt","w")
        users_store.write(str(users))
        print("Sign up succesful")
        return True
       


def notepad_function(username):
    res = input("Do you want to create a and write new notes or modify your existing notepad?\nEnter 'w' to write and 'a' to modify\n>")

    name_of_note = f"{username}.txt"
    if res.lower() == 'w':
        file = open(name_of_note, 'w')
        print("Note created succesfully")
        contents = input("Please enter your contents\n>")
        file.write(contents)
        users[username]['has_note'] =True
        print('Saved successfully')
    elif res.lower() == 'a':
        file = open(name_of_note, 'a')
        contents = input("Please enter your contents\n>")
        file.write(contents)
        print('Saved successfully')
    return







print("Welcome to Nora's Notepad")
response = input("Enter 'y' to login or 's' to sign up\n>")

username = input('Enter your username\n>')
password = input('Enter your password\n>')

if response.lower() == 'y':
    login_ = login(username, password)
    if login_:
        notepad_function(username)
        
    else:
        print("Invalid username or password")


elif response.lower() == 's':
    signup_ = signup(username, password)
    if signup_:
        notepad_function(username)





