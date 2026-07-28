# ==========================================
# PART 1: THE LIBRARIAN (Importing JSON)
# ==========================================
# JSON (JavaScript Object Notation) is a standard way to store data.
# We import the 'json' library so Python knows how to read and write these files.
import json

# Step 1: Open the filing cabinet (users.json) in "r" (Read) mode.
# 'with open' is great because it automatically closes the file when we are done!
with open("users.json", "r") as file:
    # Read the file and convert it into a Python Dictionary called 'users'
    users = json.load(file)


# ==========================================
# PART 2: THE BRAIN (The Sign-Up Function)
# ==========================================

def signUp(users):
    # Step 1: Ask for a username. 
    # We use .lower() so "Baba", "BABA", and "baba" are all treated as the same person.
    # This prevents accidental duplicates!
    username = input("Please enter your username: ").lower()
    
    # Step 2: Check if the folder already exists on our desk
    if username in users:
        print("Username already exists. Try logging in instead!")
        return # This immediately stops the function so they can't overwrite the password
        
    else:
        # Step 3: If the name is new, ask for a password
        # (Renamed the variable 'y' to 'password' so it is easier to read!)
        password = input("Enter your password: ")
        
        # Step 4: Create a new folder (Nested Dictionary) for this user on our desk
        users[username] = {
            "password": password
        }
    
    # ==========================================
    # PART 3: SAVING THE DATA
    # ==========================================
    # Step 5: Open the filing cabinet again, but this time in "w" (Write) mode.
    # Warning: "w" completely overwrites the old file with our new data!
    with open("users.json", "w") as file:
        # json.dump puts our updated 'users' dictionary back into the file.
        # 'indent=4' makes the file look neat and readable for humans, 
        # instead of squishing it all onto one line.
        json.dump(users, file, indent=4)
        
    print("User created successfully! Your data is saved.")

# ==========================================
# PART 4: TURN ON THE POWER
# ==========================================
# Run the function and pass in the dictionary we loaded at the very top.
signUp(users)