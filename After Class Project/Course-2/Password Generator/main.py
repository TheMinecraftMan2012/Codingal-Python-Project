import random
import time

def generate(name: str):
    special_char = ["!", "@", "#", "$", "%", "^", "&"]
    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    pass_char = name[:3].upper()

    password = pass_char + random.choice(special_char) + random.choice(special_char) + random.choice(number) + random.choice(number) + random.choice(number) + random.choice(special_char)

    print("Here is your password: ", password)

print("May I ask you for your name?")
name = input("Your name: ")

print(f"Hi, {name}!")
print(f"I can generate password from your name.")
print("Would you like to make a password by me?")

yesorno = input("(Y/N): ")

if yesorno == "Y" or yesorno == "y":
    time.sleep(.6)
    generate(name)

if yesorno == "n" or yesorno == "N":
    exit("Bye!")