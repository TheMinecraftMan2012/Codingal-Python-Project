from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Text Editor")
window.geometry("600x500")
window.rowconfigure(0, weight=1, minsize=800)
window.columnconfigure(1, weight=1, minsize=800)

def open_file():
    filepath = askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not filepath:
        return
    textedit.delete(1.0, END)
    with open(filepath, 'r') as file:
        text = file.read()
        textedit.insert(END, text)
        file.close()
    window.title(f"Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not filepath:
        return
    with open(filepath, 'w') as file:
        text = textedit.get(1.0, END)
        file.write(text)
    window.title(f"Text Editor - {filepath}")

textedit = Text(window)
fr_buttons = Frame(window, relief="raised", bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file, relief="groove")
btn_save = Button(fr_buttons, text="Save As...", command=save_file, relief="groove")

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
textedit.grid(row=0, column=1, sticky="nsew")

window.mainloop()