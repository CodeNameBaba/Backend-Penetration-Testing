import tkinter as tk
from tkinter import ttk



def selected():
    labelText = combo.get()
    label.config(text=labelText)



root = tk.Tk()

root.geometry("300x300")

root.title("Title Window")

label = tk.Label(root, text="Select Your City")
label.pack(pady=5)
check_var = tk.BooleanVar()
check = tk.Checkbutton(root, text="I agree to terms and conditions", font=(10), variable=check_var)

check.pack(pady=10)


choices = ["Hyderabad", "Chhapara", "Seoni", "Secunderabad"]

combo = ttk.Combobox(root, values=choices, state="readonly")
combo.set("Select A City")
combo.pack(pady=10)


btn = tk.Button(root, text="Confirm", command=selected)
btn.pack(pady=10)
root.mainloop()