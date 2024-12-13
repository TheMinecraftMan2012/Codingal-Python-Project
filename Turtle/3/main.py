import turtle

turtle.Screen().title("Stars")
turtle.Screen().bgcolor("Orange")

board = turtle.Turtle()

# First Triangle of Star

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

# Second Triangle of Star

board.pendown()

board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()