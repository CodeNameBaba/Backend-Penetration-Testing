# ==========================================
# FILE: bank.py (The Logic & Tools)
# ==========================================
import json

# --- HELPER FUNCTIONS (The Filing Clerks) ---

def save(users):
    # This function's only job is to lock the updated data in the vault.
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

def load():
    # This function fetches the data. 
    # Notice we removed the 'users' parameter because it doesn't need input to read a file!
    with open("users.json", "r") as file:
        return json.load(file)
    

# --- CORE FUNCTIONS (The Bank Staff) ---

def login(users):
    username = input("Enter Your Username: ").lower()
    password = input("Please Enter Your Password: ")

    # Check if user doesn't exist OR password is wrong
    if username not in users or password != users[username]["password"]:
        print("[ERROR] Invalid Username or password...")
        return False # Returning False tells the main menu the login failed
    else:
        print("Welcome", username)
        return username # Returning the username acts as their VIP pass


def signUp(users):
    while True:
        username = input("Enter Your Username: ").lower()
        
        if username in users:
            print("[INFO] Username Already Exists...")
        else:
            password = input("Please Enter Your Password: ")
            y = input("Please Confirm Your Password: ")

            if password == y:
                # CRITICAL FIX: We must give new users a balance, 
                # otherwise the transfer function will crash later!
                users[username] = {
                    "password": password,
                    "balance": 0
                }
                
                # Call our helper function to save the data
                save(users)
                
                print("[SUCCESS] Account created.")
                return username 
            else: 
                print("[ERROR] Your Password Does Not Match...")


def transfer(users, username):
    To = input("Who do you want to transfer to: ").lower()
    
    if To not in users:
        print("[ERROR] Username Does Not Exist...")
        return False
    elif To == username:
        print("[ERROR] You Cannot Transfer To Yourself...")
        return False
    else:
        print("You Want to transfer to", To)
        confirm = input("Please Type 'confirm' to confirm: ").lower()
        
        if confirm == "confirm":
            amount = int(input("Please Enter The Amount: "))
            
            if amount > users[username]["balance"]:
                print("[ERROR] Insufficient Balance!")
                return False
            elif amount <= 0:
                print("[ERROR] Invalid Amount...")
                return False
            else:
                # Do the math
                users[username]["balance"] -= amount
                users[To]["balance"] += amount
                
                # Save the new balances
                save(users)
                
                print("Transferred Successfully...")
                print("Your Current Balance IS: ", users[username]["balance"])
                return True
        else:
            print("Okay, Terminating Transaction...")
            return False


def resetPassword(users, username):
    while True:
        password = input("Please Enter New Password: ")
        conPass = input("Please Confirm Password: ")

        if password == conPass:
            users[username]["password"] = password
            save(users)
            print("[SUCCESS] Password Changed Successfully...")
            break
        else:
            print("[ERROR] The Passwords Do Not Match...")