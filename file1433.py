import turtle
import math
import time


def triangles(side):
    turtle.hideturtle()
    turtle.color('Black')
    turtle.fillcolor('Black')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(0, 105)
    turtle.circle(40)
    turtle.end_fill()
    turtle.begin_fill()
    turtle.goto(250, 105)
    turtle.circle(40)
    turtle.end_fill()
    turtle.begin_fill()
    turtle.goto(125, -110)
    turtle.circle(40)
    turtle.end_fill()
    turtle.goto(0, 0)
    turtle.pendown()
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)
    turtle.penup()
    y = math.sqrt((side / 3) ** 2 - (side / 6) ** 2)
    turtle.goto(side / 2, -y)
    turtle.color('white')
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.pendown()
    turtle.left(60)
    turtle.forward(side)
    for _ in range(2):
        turtle.left(120)
        turtle.forward(side)
    turtle.end_fill()


def turtle1():
    turtle.speed(0)
    triangles(250)
    time.sleep(5)

