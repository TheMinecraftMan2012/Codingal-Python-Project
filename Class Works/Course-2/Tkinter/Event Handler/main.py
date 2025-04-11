from tkinter import *

root = Tk()
root.title("Event Handler")
root.geometry("100x200")

def handle_press(event):
    print(event.char)
root.bind("<Key>", handle_press)

def handle_click(event):
    print("Button Clicked")

button = Button(root, text="Click Me")
button.pack()
button.bind("<Button-1>", handle_click)

root.mainloop()