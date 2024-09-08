import turtle
import time

t = turtle.Turtle()
screen = turtle.Screen()

screen.title("Stop Watch")
screen.bgcolor("black")

seconds, minutes, hours = 0, 0, 0

def move_silently(x = 0, y = 0):
    t.penup()
    t.goto(x, y)
    t.pendown()

t.speed(0)

def layout():
    t.penup()
    t.goto(-80, 100)
    t.pensize(3)
    t.pencolor("white")
    # t.write("STOP WATCH")
    t.goto(-100, 40)
    t.pendown()
    # for _ in range(2):
    #     t.forward(200)
    #     t.right(90)
    #     t.forward(60)
    #     t.right(90)

    t.pencolor("green")

    move_silently(-70, 15)
    t.write("hh", font=50)
    move_silently(-70, -10)
    t.write(hours, font=50)

    move_silently(-50, -7)
    t.write(":", font=50)

    move_silently(-35, 15)
    t.write("mm", font=50)
    move_silently(-35, -10)
    t.write(minutes, font=50)

    move_silently(-12, -7)
    t.write(":", font=50)

    move_silently(0, 15)
    t.write("ss", font=50)
    move_silently(5, -10)
    t.write(seconds, font=50)

def seconds_tick(s):
    while True:
        s += 1
        time.sleep(1)
        t.undo()
        t.write(s, font=50)

layout()

seconds_tick(10)

turtle.done()
