from tkinter import *
from datetime import date

root = Tk()
root.title('Getting started with widgets')
root.geometry("400x300")

lbl = Label(text="Hey there!", fg="white", bg="#872F5F", height=1, width=300)

name_lbl = Label(text="Full name", bg="#389503")
name_entry = Entry()

def display():
    name = name_entry.get()

    global message
    message = "Welcome to the Application! \n Today's date is: "
    greet = "Hello " + name + "\n"

    date_splited = str(date.today()).split("-")
    datenow = date_splited[2] + "/" + date_splited[1] + "/" + date_splited[0]

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, datenow)

text_box = Text(height=3)

button = Button(text="Begin", command=display, height=1, bg="#1261A0", fg="white")

lbl.pack()
name_lbl.place()
name_entry.pack()
button.pack()
text_box.pack()

root.mainloop()