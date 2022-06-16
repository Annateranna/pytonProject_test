import turtle
from math import *
import time


def turtle1():
    turtle.Screen().setup(400, 400)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.fillcolor('Red')
    turtle.begin_fill()
    turtle.pencolor('Red')
    turtle.pendown()
    t = 0
    while t <= 2 * pi + 0.1:
        x = 128 * sin(t) ** 3
        y = 8 * (13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t) - 5)
        turtle.goto(x, y)
        t += 0.1
    turtle.end_fill()
    time.sleep(5)
