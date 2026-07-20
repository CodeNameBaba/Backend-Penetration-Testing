#GUI Using Tkinter Library



# Importing a library
import tkinter

def showName():
    text = userInput.get()
    userInput.delete(0,tkinter.END)
    label.config(text=text, font=("Arial", 10, "bold"), fg="green")

# Creating a window

root = tkinter.Tk()


root.title("Shahwar")

# Adjusting the size of the generated window
root.geometry("500x200")

# Adding A Text Inside Our Generated Window
label = tkinter.Label(root, text="Enter Your Name", font=("Arial", 10), fg="blue")

label.grid(row=0, column=0, padx=5)
# Taking Input From The User

userInput = tkinter.Entry(root)
userInput.grid(row=1,column=0, padx=5)

#Buttons

button1 = tkinter.Button(root, text="Press Me", command=showName)
button1.grid(row=2, column=0)


root.mainloop()