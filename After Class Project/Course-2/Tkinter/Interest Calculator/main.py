from tkinter import *

def compound_interest(p, r, n, t):
    a = p * (1 + (r / n * 100)) ** (n * t)
    return a

def simple_interest(p, r, n):
    i = p * r * n
    i = i + p
    return i

def calculate_interest():
    try:
        p = float(principal_amount.get())
        r = float(rate.get()) / 100
        n_s = float(time.get())
        n_c = int(compound_time.get())

        smp_interest_txt.delete(1.0, END)
        smp_interest_txt.insert(END, "Calculated S.I\n")
        smp_interest_txt.insert(END, "With Interest: " + str(simple_interest(p, r, n_s)) + "\n")
        smp_interest_txt.insert(END, "Without Interest: " + str(simple_interest(p, r, n_s) - p))

        cmp_interest_txt.delete(1.0, END)
        cmp_interest_txt.insert(END, "Calculated C.I\n")
        cmp_interest_txt.insert(END, "With Interest: " + str(compound_interest(p, r, n_s, n_c)) + "\n")
        cmp_interest_txt.insert(END, "Without Interest: " + str(compound_interest(p, r, n_s, n_c) - p))
    except Exception as e:
        print(e)

window = Tk()
window.title("Interest Calculator")
window.geometry("400x400")

input_frame = Frame(window)
input_frame.pack()

lbl_principal = Label(input_frame, text="Principal Amount", font=("Arial", 12, "bold"), background="lightblue", width=40)
lbl_principal.pack()

principal_amount = Entry(input_frame, width=66)
principal_amount.pack()

lbl_rate = Label(input_frame, text="Rate (In Percent)", font=("Arial", 12, "bold"), background="lightblue", width=40)
lbl_rate.pack()

rate = Entry(input_frame, width=66)
rate.pack()

lbl_time = Label(input_frame, text="Time (In Years)", font=("Arial", 12, "bold"), background="lightblue", width=40)
lbl_time.pack()

time = Entry(input_frame, width=66)
time.pack()

lbl_compound = Label(input_frame, text="Number of times interest is compounded per year", font=("Arial", 12, "bold"), background="lightblue", width=40)
lbl_compound.pack()

compound_time = Entry(input_frame, width=66)
compound_time.pack()

txt_frame = Frame(window, relief="sunken")
txt_frame.columnconfigure(0)
txt_frame.columnconfigure(1)
txt_frame.pack()

smp_interest_txt = Text(txt_frame, relief="sunken", height=5, width=24)
smp_interest_txt.grid(column=0, row=0)

cmp_interest_txt = Text(txt_frame, relief="sunken", height=5, width=24)
cmp_interest_txt.grid(column=1, row=0)

calculate = Button(window, relief="groove", text="Calculate", command=calculate_interest)
calculate.pack(pady=30)

window.mainloop()