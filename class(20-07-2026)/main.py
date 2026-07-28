import tkinter

# ==========================================
# PART 1: THE BRAIN (Functions)
# ==========================================
# This is the action that triggers when the "Press Me" button is clicked.

def showName():
    # Step 1: Read the text the user typed into the blank Entry box
    text = userInput.get()
    
    # Step 2: Use an eraser! Delete the text in the box from the beginning (0) 
    # all the way to the END, so it's completely clean for the next person.
    userInput.delete(0, tkinter.END)
    
    # Step 3: Change our label's configuration to show the secret message they typed!
    # We also change the font to be "bold" and the color (fg, or foreground) to green.
    label.config(text=text, font=("Arial", 10, "bold"), fg="green")


# ==========================================
# PART 2: THE CLIPBOARD (Main Window Setup)
# ==========================================
root = tkinter.Tk()

# Set the text at the top of the window border
root.title("Shahwar")

# Adjusting the size of the generated window (Width x Height)
root.geometry("500x200")


# ==========================================
# PART 3: THE WIDGETS & THE GRID (Building the Form)
# ==========================================
# IMPORTANT: We are using .grid() instead of .pack() here!
# We must specify the exact row and column for every single item.
# Note: 'padx=5' just adds 5 pixels of breathing room on the left and right.

# --- WIDGET 1: A Label (Simple Text) ---
label = tkinter.Label(root, text="Enter Your Name", font=("Arial", 10), fg="blue")
# Put this in the very top-left corner (Row 0, Column 0)
label.grid(row=0, column=0, padx=5)


# --- WIDGET 2: An Entry (A fill-in-the-blank box) ---
userInput = tkinter.Entry(root)
# Put this right beneath the label (Row 1, Column 0)
userInput.grid(row=1, column=0, padx=5)


# --- WIDGET 3: A Button ---
# We wire this button to the 'showName' brain we built at the top
button1 = tkinter.Button(root, text="Press Me", command=showName)
# Put this right beneath the Entry box (Row 2, Column 0)
button1.grid(row=2, column=0)


# ==========================================
# PART 4: TURN ON THE POWER
# ==========================================
# Keep the window running and listening for clicks
root.mainloop()
