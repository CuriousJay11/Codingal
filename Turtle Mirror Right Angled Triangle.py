import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(1)

# Draw a mirrored right-angled triangle
t.penup()
t.goto(100, -100)  # Starting from bottom right
t.pendown()

t.goto(0, -100)    # Base to the left
t.goto(100, 0)     # Hypotenuse
t.goto(100, -100)  # Back to start

# Hide turtle and display the window
t.hideturtle()
turtle.done()