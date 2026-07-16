#15/07/2026

import json

# Add Users.json into a variable u sers

with open("users.json", "r") as file:
    users = json.load(file)


#Login function that takes users.json and returns username
def login(users):
    username = input("Enter Your Username: ").lower()
    password = input("Please Enter Your Password: ")

    if username not in users or password != users[username]["password"]:
        print("Invalid Username or password...")
        return
    else:
        print("Welcome", username)
        return username 


# Creating A SignUp Function As Well that takes users.json in parameters and returns the username 
def signUp(users):
    while True:
        username = input("Enter Your Username: ").lower()
        if username in users:
            print("Username Already Exists...")
        else:
            password = input("Please Enter Your Password: ")
            y = input("Please Confirm Your Password: ")

            if password == y:
                users[username] = {
                    "password": password
                }
                
                with open("users.json", "w") as file:
                    json.dump(users, file, indent=4)
                    print("Account Created Succesfully...")
                return username
                break
            else: 
                print("Your Password Does Not Match...")

def transfer(users, username):
    To = input("Who do you want to transfer: ").lower()
    if To not in users:
        print("Username Does Not Exists...")
        return
    elif To == username:
        print("You Cannot Transfer To Yourself...")
        return
    else:
        print("You Want to transfer to", To)
        confirm = input("Please Type confirm to confirm: ").lower()
        if confirm == "confirm":
            amount = int(input("Please Enter The Amount: "))
            if amount > users[username]["balance"]:
                print("Insufficient Balance!")
                return
            elif amount <= 0:
                print("Invalid Amount...")
            else:
                users[username]["balance"] -= amount
                users[To]["balance"] += amount
                with open("users.json", "w") as file:
                    json.dump(users, file, indent=4)
                print("Tranferred Successfully...\n Your Current Balance IS: ", users[username]["balance"])



# username = login(users)

# transfer(users, username)