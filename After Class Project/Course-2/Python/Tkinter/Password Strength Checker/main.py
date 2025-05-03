import tkinter as tk
from tkinter import StringVar

# Function to check strength
def check_password_strength(password: str) -> str:
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(not char.isalnum() for char in password):
        strength += 1

    if strength <= 1:
        return "Weak"
    elif strength == 2 or strength == 3:
        return "Medium"
    else:
        return "Strong"

# Update function
def update_strength(*args):
    pwd = password_var.get()
    result = check_password_strength(pwd)
    strength_var.set(f"Strength: {result}")

    # Change color
    if result == "Weak":
        strength_label.config(fg="red")
    elif result == "Medium":
        strength_label.config(fg="orange")
    else:
        strength_label.config(fg="green")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

password_var = StringVar()
password_var.trace_add('write', update_strength)

strength_var = StringVar()
strength_var.set("Strength: ")

# Widgets
title = tk.Label(root, text="Enter Password:", font=("Arial", 14))
title.pack(pady=10)

entry = tk.Entry(root, textvariable=password_var, width=30, font=("Arial", 12))
entry.pack(pady=5)

strength_label = tk.Label(root, textvariable=strength_var, font=("Arial", 14))
strength_label.pack(pady=10)

# Start GUI
root.mainloop()
