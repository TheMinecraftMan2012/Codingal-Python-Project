import turtle

screen = turtle.Screen()
board = turtle.Turtle()

## Setting up the app ##
screen.title("Drawing Shapes Using Turtle")
screen.bgcolor("skyblue")

## Drawing Triangle ##
board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.forward(200)
board.right(240)
board.pendown()

## Drawing Rectangle ##
board.left(90)
board.forward(100)

board.left(90)
board.forward(150)

board.left(90)
board.forward(100)

board.left(90)
board.forward(150)

turtle.done()