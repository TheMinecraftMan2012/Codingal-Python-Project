from tkinter import *

window = Tk()
window.title("Inches to Centimeters")
window.geometry("400x400")
window.resizable(0, 0)

def inches_to_cm():
    inches_value = float(inches.get())
    cm_value = inches_value * 2.54

    textarea.insert(END, "Hey User!")
    textarea.insert(END, f"\nConverstion of {inches_value}inch to cm is {cm_value}cm")

lbl1 = Label(window, text="Enter Length in Inches", font=("Arial", 12))
lbl1.pack(pady=20)

inches = Entry(window, width=50)
inches.pack(pady=10)

button = Button(window, text="Convert", relief="groove", command=inches_to_cm)
button.pack(pady=10)

textarea = Text(window, width=50, height=10, bg="#BEBEBE", fg="black")
textarea.pack(pady=10)

window.mainloop()