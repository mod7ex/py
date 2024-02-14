import turtle

COLORS = ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]

t = turtle.Turtle()
screen = turtle.Screen()

screen.title("Spirograph circle")

screen.bgcolor("black")

t.pensize(2)

t.speed(0)

for i in range(6):
    for color in COLORS:
        t.color(color)
        t.circle(100)
        t.left(10)

t.hideturtle()

turtle.done()