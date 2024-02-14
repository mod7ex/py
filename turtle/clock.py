import turtle

t = turtle.Turtle()
screen = turtle.Screen()

screen.title("Clock")
screen.bgcolor("black")
t.pencolor("blue")

def move_silently(x = 0, y = 0):
    t.penup()
    t.goto(x, y)
    t.pendown()

x, y = 0, 0

radius = 200
thickness = 50 

# t.speed(0)

t.home()
# t.write((x, y))

t.begin_fill()
t.fillcolor("blue")

y = -radius
move_silently(x, y)
t.circle(radius)

y += thickness
move_silently(x, y)
t.circle(radius - thickness)

t.end_fill()

move_silently()
t.left(90)

t.pencolor("white")

for i in range(12):
    t.right(360/12)
    t.penup()
    t.forward(i*(11-i)/2 + radius - thickness/2) # <i*(11-i)/2> is for the small deviation error
    t.pendown()
    t.write((i+1))
    move_silently()


def draw_hour_arm():
    t.pensize(5)
    t.right(180)
    t.forward(radius*0.6)

draw_hour_arm()

move_silently()
t.setheading(90)

def draw_minute_arm():
    t.pensize(3)
    t.right(270)
    t.forward(70)

draw_minute_arm()

move_silently()
t.setheading(90)

t.hideturtle()

turtle.done()