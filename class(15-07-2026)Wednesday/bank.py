import json

# ==========================================
# PART 1: THE BOUNCER & THE REGISTRAR
# ==========================================

def login(users):
    username = input("\n[LOGIN] Enter Your Username: ").lower()
    password = input("[LOGIN] Enter Your Password: ")

    if username not in users or password != users[username]["password"]:
        print("❌ Invalid Username or password.")
        return None 
    else:
        print(f"✅ Login successful! Welcome back, {username}.")
        return username 

def signUp(users):
    while True:
        username = input("\n[SIGN UP] Enter a New Username (or type 'cancel'): ").lower()
        
        if username == 'cancel':
            return None
            
        if username in users:
            print("❌ Username Already Exists...")
        else:
            password = input("[SIGN UP] Create a Password: ")
            y = input("[SIGN UP] Confirm Your Password: ")

            if password == y:
                # 🌟 NEW CONCEPT: We add a 'history' List ([]) to track their receipts!
                users[username] = {
                    "password": password,
                    "balance": 0,
                    "history": ["Account created."]
                }
                
                with open("users.json", "w") as file:
                    json.dump(users, file, indent=4)
                    
                print("✅ Account Created Successfully!")
                return username 
            else: 
                print("❌ Passwords Do Not Match... Let's try again.")


# ==========================================
# PART 2: THE TELLER WINDOW (Banking Features)
# ==========================================

def check_balance(users, username):
    print(f"\n Your current balance is: ₹{users[username]['balance']}")
    print("--- Recent Transactions ---")
    
    #  NEW CONCEPT: Looping through a list to show history
    for receipt in users[username]["history"]:
        print(f"- {receipt}")
    print("---------------------------")


def deposit(users, username):
    #  NEW CONCEPT: The Safety Net (Try/Except)
    # If the user types "five" instead of "5", int() usually crashes the program.
    # 'try' tells Python to attempt the math. If it fails, the 'except' block catches the crash!
    try:
        amount = int(input("How much would you like to deposit? ₹"))
        if amount <= 0:
            print(" Invalid amount.")
            return
            
        users[username]["balance"] += amount
        
        # Add a receipt to their history list!
        receipt = f"Deposited ₹{amount}"
        users[username]["history"].append(receipt)
        
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)
            
        print(f" Deposited successfully! New balance: ₹{users[username]['balance']}")
        
    except ValueError:
        print(" Error: Please enter numbers only! No text allowed.")

def transfer(users, username):
    To = input("Who do you want to transfer money to? ").lower()
    
    if To not in users:
        print(" Username Does Not Exist...")
        return
    elif To == username:
        print(" You Cannot Transfer To Yourself...")
        return
        
    try:
        amount = int(input(f"Enter amount to send to {To}: ₹"))
        
        if amount > users[username]["balance"]:
            print(" Insufficient Balance!")
        elif amount <= 0:
            print(" Invalid Amount.")
        else:
            # Move the money
            users[username]["balance"] -= amount
            users[To]["balance"] += amount
            
            # Write the receipts for BOTH users!
            users[username]["history"].append(f"Sent ₹{amount} to {To}")
            users[To]["history"].append(f"Received ₹{amount} from {username}")
            
            with open("users.json", "w") as file:
                json.dump(users, file, indent=4)
                
            print(f" Transferred Successfully! Your new balance is: ₹{users[username]['balance']}")
            
    except ValueError:
        print(" Error: Please enter numbers only!")