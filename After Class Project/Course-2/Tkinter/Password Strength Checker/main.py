from tkinter import *
from tkinter import messagebox

def check():
    password = password_entry.get()
    if password == "":
        messagebox.showinfo("Alert", "Please don't leave the entry blank")
    else:
        ch_1 = []

root = Tk()
root.geometry("400x300")
root.title("Password Strength Checker")

Label(root, text="Password Strength Checker", font=("Arial", 18, "bold")).pack(pady=10)

Label(root, text="Your Password", font=("Arial", 14)).pack(pady=7)
password_entry = Entry(root, width=50)
password_entry.pack(pady=8)
Button(root, text="Check Password", relief=GROOVE, command=check).pack(pady=5)

result = Label(root, text="", font=("Arial", 13))
result.pack(pady=12)

root.mainloop()