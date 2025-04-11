from tkinter import *

root = Tk()

root.geometry("450x350")
root.title('Product')

def product():
    p1 = float(num1_entry.get())
    p2 = float(num2_entry.get())
    pN = float(prodNum.get())

    message = f"Product of {p1} and {p2} is: \n"
    product = f"{p1 * pN} and {p2 * pN} \n"
    product2 = f"{p1} * {p2} = {p1 * p2}"

    textbox.insert(END, message)
    textbox.insert(END, product)
    textbox.insert(END, product2)

num1_entry = Entry()
num2_entry = Entry()
prodNum = Entry()
button = Button(text="Product", command=product)
textbox = Text(height=4)

Label(text="Number1 Here", fg="white", bg="#5462ff", width="300").pack()
num1_entry.pack()
Label(text="Number2 Here", fg="white", bg="#5462ff", width="300").pack()
num2_entry.pack()
Label(text="Producting Number", fg="white", bg="#5462ff", width="300").pack()
prodNum.pack()
button.pack()
textbox.pack()

root.mainloop()