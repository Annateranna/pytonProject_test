import turtle
import random


def stars(s, c, p):
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.pencolor(c)
    angle = 180 - 180 / p
    for i in range(p):
        turtle.forward(s)
        turtle.right(angle)
    turtle.end_fill()


def left_mouse_click(x, y):
    s = random.randint(5, 20)
    c = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    p = random.randint(2, 5) * 2 + 1
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    stars(s, c, p)


turtle.Screen().setup(600, 600)
turtle.Screen().colormode(255)
turtle.speed(0)
turtle.Screen().bgcolor('Black')
turtle.Screen().onclick(left_mouse_click, btn=1, add=None)
turtle.hideturtle()
turtle.done()

