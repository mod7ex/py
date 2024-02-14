import turtle

t = turtle.Turtle()

t.screen.bgcolor("black")
t.pensize(2)
t.color("green")

t.speed(0)

t.left(90)

t.backward(100)

# t.shape('turtle')

def tree(i):
    if i >= 10:
        t.forward(i)
        t.color("orange")
        t.circle(2)
        t.color("brown")
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)
    else:
        return

t.hideturtle()

tree(100)

turtle.done()