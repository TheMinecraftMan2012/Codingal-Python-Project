import turtle
import random

colors = ["red", "blue", "green", "yellow", "pink", "orange", "skyblue", "gold", "aliceblue", "tomato"]

screen = turtle.Screen()

screen.bgcolor(random.choice(colors))
screen.title("Square")

for i in range(4):
    turtle.forward(70)
    turtle.right(90)

turtle.done()