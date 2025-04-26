from tkinter import *

root = Tk()
root.title("Main Window")
root.geometry("400x300")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("Top Level Window")

    lbl2 = Label(top, text="This is the Top Level Window")
    lbl2.pack()

lbl = Label(root, text="This is the main window")
button = Button(root, text="Open Top Level", command=topwin)

lbl.pack()
button.pack()

root.mainloop()