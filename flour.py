import turtle

t = turtle.Turtle()

t.speed(0)

def fleur():
    for i in range(300):
        t.circle(190 - i, 90)
        t.left(90)
        t.circle(190 - i, 90)
        t.left(18)

fleur()

# t.screen.mainloop()

t.hideturtle()

turtle.done()