import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.title("3D CUBE")
s.screensize(800, 500, bg="black")

t.pencolor("white")
t.pensize(3)

a = 100
angle = 30

def move_silently(x = 0, y = 0):
    t.penup()
    t.goto(x, y)
    t.pendown()

def square(len):
    for _ in range(4):
        t.forward(len)
        t.left(90)

def inclined_side(len):
    t.forward(len)

def draw_inclined_sides():
    t.left(angle)
    for i in range(0, 4):
        x, y = 0, 0
        match i:
            case 1:
                y = 1
            case 2:
                x, y = 1, 1
            case 3:
                x = 1
        move_silently(x*a, y*a)
        inclined_side(a*2)

draw_inclined_sides()

# reset
t.right(angle)
move_silently()

square(a)

t.penup()
t.left(angle)
t.forward(a*2)
t.right(30)
t.pendown()

square(a)
    
t.hideturtle()

turtle.done()