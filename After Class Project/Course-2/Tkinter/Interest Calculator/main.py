from tkinter import *

window = Tk()
window.title("Interest Calculator")
window.geometry("445x445")
# window.resizable(False, False)

input_frame = Frame(window, relief="raised", bd=2, background="#f0f0f0")
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)
input_frame.pack()

txt_frame = Frame(window, relief="raised", bd=2)
txt_frame.columnconfigure(0, weight=1)
txt_frame.columnconfigure(1, weight=1)
txt_frame.pack()

slp_interest_txt = Text(txt_frame, background="#f0f0f0", width=27, height=10)
slp_interest_txt.grid(row=1, column=0)

cmp_interest_txt = Text(txt_frame, background="#f0f0f0", width=27, height=10)
cmp_interest_txt.grid(row=1, column=1)

window.mainloop()