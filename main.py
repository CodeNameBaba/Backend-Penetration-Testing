#25/07/2026
import json

with open("users.json", "r") as file:
    users = json.load(file)

def signUp(users):
    username = input("Please enter your username: ").lower()
    if username in users:
        print("Username already exists")
        return
    else:
        y = input("Enter your password: ")
        

        users[username]= {
            "password":y
        }
    
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)
    print("User created succesfully...")


signUp(users)