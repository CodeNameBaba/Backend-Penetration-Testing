import bank as m
import json
import time
import os

with open("users.json", "r") as file:
    users = json.load(file)

users = m.load(users)

print("Welcome to Vijay Balya Bank")

while True:
    print("To Login Press 1\nTo SignUp Press 2")
    x = int(input("Enter Here: "))
    if x == 1:
        username = m.login(users)
        if username == False:
            print("Please Retry...")
        else:
            break
    elif x == 2:
        username = m.signUp(users)
        break
    else:
        print("Invalid...")

while True:
    print("To Transfer Money To Another Person Press 1\nTo Change Password Press 2")
    choice = input("Enter Your Choice:  ")
    if choice =="1":
        x = m.transfer(users, username)
        if x == False:
            print("Redirecting To Previous Menu...")
            time.sleep(1.5)
            os.system("cls")
        elif x == True:
            break

    elif choice == "2":
        m.resetPassword(users,username)
        break
    else:
        print("Invalid Choice...")