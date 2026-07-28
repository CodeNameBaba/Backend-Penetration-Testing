# ==========================================
# FILE: main.py (The User Interface)
# ==========================================
import bank as m
import time
import os

# Step 1: Use our helper function to load the data right away
users = m.load()

print("Welcome to Vijay Balya Bank")

# ==========================================
# THE LOBBY (Login / Sign Up Loop)
# ==========================================
while True:
    print("\nTo Login Press 1\nTo SignUp Press 2")
    
    # We use string input instead of int() to prevent crashes if they type a letter
    x = input("Enter Here: ") 
    
    if x == "1":
        # The login function either returns the username or False
        username = m.login(users)
        
        if username == False:
            print("Please Retry...")
        else:
            break # Success! Break out of the lobby loop.
            
    elif x == "2":
        username = m.signUp(users)
        break # Success! Break out of the lobby loop.
        
    else:
        print("[ERROR] Invalid Input...")


# ==========================================
# THE ACCOUNT MENU (Transfer / Password Loop)
# ==========================================
# If they broke out of the first loop, they are officially logged in!

while True:
    print("\n--- ACCOUNT MENU ---")
    print("To Transfer Money To Another Person Press 1")
    print("To Change Password Press 2")
    print("To Logout Press 3")
    
    choice = input("Enter Your Choice:  ")
    
    if choice == "1":
        # Transfer returns True if it works, False if it fails
        result = m.transfer(users, username)
        
        if result == False:
            print("Redirecting To Previous Menu...")
            time.sleep(1.5) # Pause the program for 1.5 seconds
            
            # This clears the terminal screen (Windows uses 'cls', Mac/Linux uses 'clear')
            # It makes the app look clean and professional!
            os.system("cls") 
            
        elif result == True:
            # We don't necessarily want to break and close the app just because 
            # they transferred money. We can just let the loop continue!
            input("Press Enter to return to menu...")
            os.system("cls")

    elif choice == "2":
        m.resetPassword(users, username)
        input("Press Enter to return to menu...")
        os.system("cls")
        
    elif choice == "3":
        print("Logging out. Goodbye!")
        time.sleep(1)
        os.system("cls")
        break # This breaks the final loop, closing the program.
        
    else:
        print("[ERROR] Invalid Choice...")