import turtle

t = turtle.Turtle()

screen = turtle.Screen()

screen.bgcolor("black")
t.pencolor("blue")

t.speed(0)

count = 0
step_angle = 5
d = 0

while True:
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.right(step_angle)
    count += 1
    if count >= 390/step_angle:
        t.forward(80)
        count = 0
        d += 1
        if d >= 12:
            break

t.hideturtle()

turtle.done()