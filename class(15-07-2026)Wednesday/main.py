import json

# ==========================================
# PART 1: THE VAULT (Loading the Data)
# ==========================================
# We start by bringing the filing cabinet (JSON) onto our desk (Python Dictionary)

with open("users.json", "r") as file:
    users = json.load(file)


# ==========================================
# PART 2: THE BOUNCER (Login Function)
# ==========================================
# Takes the 'users' dictionary. Returns the 'username' if successful.

def login(users):
    username = input("Enter Your Username: ").lower()
    password = input("Please Enter Your Password: ")

    # Check two things: Is the user NOT in the database? OR is the password wrong?
    if username not in users or password != users[username]["password"]:
        print("Invalid Username or password...")
        return None # Return None means they don't get a VIP pass
    else:
        print(f"Welcome to the Bank, {username}!")
        return username # Hand them their VIP pass!


# ==========================================
# PART 3: THE REGISTRAR (Sign-up Function)
# ==========================================
def signUp(users):
    # 'while True' creates an infinite loop. They are trapped here until they succeed!
    while True:
        username = input("Enter Your Username: ").lower()
        
        if username in users:
            print("Username Already Exists... Try a different one.")
        else:
            password = input("Please Enter Your Password: ")
            y = input("Please Confirm Your Password: ")

            # Check if the passwords match
            if password == y:
                # NOTE: We MUST give new users a starting balance, 
                # otherwise our transfer function will crash later!
                users[username] = {
                    "password": password,
                    "balance": 0 
                }
                
                # Save the new user to the JSON file
                with open("users.json", "w") as file:
                    json.dump(users, file, indent=4)
                    
                print("Account Created Successfully...")
                
                # 'return' automatically breaks out of a while loop and passes the value back.
                # Note: Any code written below a 'return' statement is completely ignored!
                return username 
            else: 
                print("Your Passwords Do Not Match... Let's try again.")


# ==========================================
# PART 4: THE BANK TELLER (Transfer Function)
# ==========================================
# This function requires the VIP pass ('username') so it knows who is sending the money!

def transfer(users, username):
    To = input("Who do you want to transfer money to? ").lower()
    
    # 1. Security Check: Does the receiver exist?
    if To not in users:
        print("Username Does Not Exist...")
        return
        
    # 2. Security Check: Are they sending money to themselves?
    elif To == username:
        print("You Cannot Transfer To Yourself...")
        return
        
    else:
        print(f"You want to transfer to {To}.")
        confirm = input("Please type 'confirm' to proceed: ").lower()
        
        if confirm == "confirm":
            # Convert input to integer so we can do math!
            amount = int(input("Please Enter The Amount: "))
            
            # 3. Math Check: Do they have enough money?
            if amount > users[username]["balance"]:
                print("Insufficient Balance! Transfer failed.")
                return
                
            # 4. Math Check: Did they type a negative number or zero?
            elif amount <= 0:
                print("Invalid Amount... Cannot transfer zero or negative money.")
                
            else:
                # 5. THE TRANSACTION
                # Deduct from the sender
                users[username]["balance"] -= amount
                # Add to the receiver
                users[To]["balance"] += amount
                
                # 6. SAVE TO VAULT
                with open("users.json", "w") as file:
                    json.dump(users, file, indent=4)
                    
                print("Transferred Successfully!")
                print(f"Your Current Balance Is: {users[username]['balance']}")