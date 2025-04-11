from tkinter import *
from datetime import *

root = Tk()
root.title("Age Calculator")
root.geometry("400x400")

def calculate_age():
    birth_date = datetime.strptime(birthdate_entry.get(), "%d/%m/%Y")
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    result_lbl['text'] = f"Your Age is {age} years"

lbl1 = Label(text="Age Calculator", font=("Times New Roman", 20), fg="black")
lbl1.pack(pady=20)

lbl2 = Label(text="Enter your birthdate as DD/MM/YYYY", font=("Times New Roman", 15), fg="black")
lbl2.pack(pady=5)

birthdate_entry = Entry(root, width=50)
birthdate_entry.pack(pady=5)

button = Button(root, text="Calculate Age", relief="groove", command=calculate_age)
button.pack(pady=10)

result_lbl = Label(root, text="Your Result Here", font=("Times New Roman", 15), fg="black")
result_lbl.pack(pady=50)

root.mainloop()