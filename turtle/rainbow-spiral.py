import turtle

t = turtle.Turtle()
screen = turtle.Screen()

screen.title("Rainbow spiral")
screen.bgcolor("black")

t.speed(0)

r, g, b = 255, 0, 0

for i in range(255*2):
    screen.colormode(255) # set color mode 
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        b+=3
    elif i<255*4//3:
        g-=3
    elif i<255*5//3:
        r+=3
    else:
        b-=3
    t.forward(50+i)
    t.right(91)
    t.pencolor(r,g,b)

t.hideturtle()

turtle.done()