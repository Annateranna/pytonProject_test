import turtle
import math
import time


def triangles(side):
    turtle.hideturtle()
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)
    turtle.penup()
    y = math.sqrt((side / 3) ** 2 - (side / 6) ** 2)
    turtle.goto(side / 2, -y)
    turtle.pendown()
    turtle.left(60)
    turtle.forward(side)
    for _ in range(2):
        turtle.left(120)
        turtle.forward(side)


def turtle1():
    turtle.speed(0)
    triangles(200)
    time.sleep(5)
