import time
import random

number = random.randint(1, 100)

def intro():
    print("May I ask you for your name?")
    global name
    name = input("Enter your name: ")
    print(f"Hi, {name}! Today we're going to play number guessing between 1 to 100")

    if number % 2 == 0:
        x = "even"
    else:
        x = "odd"

    print(f"Hint: The chosen number is an {x} number")

def pick():
    guessTaken = 0

    while guessTaken < 6:
        time.sleep(0.25)
        enter = input("Guess: ")

        try:
            guess = int(enter)
            
            if guess <= 100 and guess >= 1:
                guessTaken = guessTaken + 1
                if guessTaken < 6:
                    if number > guess:
                        print("The entered number is too high!")
                    if number < guess:
                        print("The Entered number is too low!")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                    if guess == number:
                        break
            
            if guess > 100 or guess < 1:
                print("Silly Goose! That number is not in the range.")
                time.sleep(.25)
                print("Please enter a number between 1 and 100")
        
        except:
            print("Sorry, but I don't think that is a number.")
    
    if guess == number:
        print(f"Good job, {name}! You have guessed my number in {guessTaken} guesses.")
    if guess != number:
        print(f"Nope! The number I was thinking is {number}")

playagain = "yes"

while playagain == "yes" or playagain == "y" or playagain == "Yes":
    intro()
    pick()
    print("Do you want to play again?")
    playagain = input()