import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(300,300)

square = turtle.Turtle()

for i in range(4):
    square.forward(100)
    square.left(90)

turtle.done()