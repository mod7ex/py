import turtle
import time

t = turtle.Turtle()

def box(ln, isBlack):
    t.begin_fill()
    if isBlack:
        t.fillcolor("black")
    else:
        t.fillcolor("white")
    for _ in range(0, 4):
        t.forward(ln)
        t.left(90)
    t.end_fill()

box_len = 50

x, y = 0, 0

time.sleep(2) # Start drawing

t.speed(0)

def move_silently(x = 0, y = 0):
    t.penup()
    t.goto(x, y)
    t.pendown()

while True:
    move_silently(x, y)
    x += box_len

    is_black = False
    x_index = 1 + x/box_len
    y_index = 1 + y/box_len
    if (x_index%2 == 0 and y_index%2 == 0) or x_index * y_index % 2 != 0:
        is_black = True

    box(box_len, is_black)

    if x >= 8 * box_len:
        x = 0
        y += box_len
        if y >= box_len * 8:
            break

t.hideturtle()

turtle.done()

