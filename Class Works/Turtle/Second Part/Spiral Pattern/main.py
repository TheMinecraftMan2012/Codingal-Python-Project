import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

screen.bgcolor("orange")
screen.title("Spiral Pattern")

pen.speed(5)

size = 0

while True:
    for i in range(4):
        pen.fd(size + 1)
        pen.left(90)
        size = size - 5
    
    size = size + 1