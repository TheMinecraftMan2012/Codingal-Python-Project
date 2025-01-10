import turtle

screen = turtle.Screen()
polygon = turtle.Turtle()

screen.bgcolor("orange")
screen.title("Polygon")

length = 70
sides = 6
angle = 360.0 / sides

for i in range(sides):
    polygon.forward(length)
    polygon.right(angle)

turtle.done()