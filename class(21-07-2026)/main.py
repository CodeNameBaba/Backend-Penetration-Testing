import tkinter as tk
from tkinter import ttk

# ==========================================
# PART 1: THE BRAIN (Functions)
# ==========================================
# This function is the "action" that happens when the button is clicked.
# It doesn't run until the button specifically calls it.

def selected():
    # Step 1: Grab the current text sitting inside the dropdown menu (combo)
    labelText = combo.get()
    
    # Step 2: Change the configuration (settings) of our label 
    # to display the text we just grabbed.
    label.config(text=labelText)


# ==========================================
# PART 2: THE CLIPBOARD (Main Window Setup)
# ==========================================

# Create the main, blank window (our clipboard)
root = tk.Tk()

# Set the size of the window (Width x Height)
root.geometry("300x300")

# Set the text that appears at the very top of the window border
root.title("Title Window")


# ==========================================
# PART 3: THE WIDGETS (Building the Form)
# ==========================================

# --- WIDGET 1: A Label (Simple Text) ---
label = tk.Label(root, text="Select Your City")
# Glue it to the window with 5 pixels of padding (empty space) on the top/bottom (y-axis)
label.pack(pady=5)


# --- WIDGET 2: A Checkbox ---
# Tkinter needs special variables to track if a box is checked (True) or unchecked (False)
check_var = tk.BooleanVar() 
check = tk.Checkbutton(root, text="I agree to terms and conditions", font=(10), variable=check_var)
check.pack(pady=10)


# --- WIDGET 3: A Combobox (Dropdown Menu) ---
# First, create a standard Python list of our options
choices = ["Hyderabad", "Chhapara", "Seoni", "Secunderabad", "Delhi"]

# Create the dropdown. 'readonly' means the user can't type their own fake city into the box.
combo = ttk.Combobox(root, values=choices, state="readonly")
# Set the default placeholder text before they click anything
combo.set("Select A City") 
combo.pack(pady=10)


# --- WIDGET 4: A Button ---
# We use 'command=selected' to wire this button to the function we wrote at the top.
# Notice we DO NOT use parentheses () after 'selected'. We are just pointing to it, not running it yet!
btn = tk.Button(root, text="kaxim", command=selected)
btn.pack(pady=10)


# ==========================================
# PART 4: TURN ON THE POWER
# ==========================================
# This tells the computer to keep the window open and constantly listen 
# for mouse clicks, typing, or scrolling. Without this, the window opens and closes instantly.
root.mainloop()
