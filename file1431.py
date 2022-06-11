import turtle
import math
import time


def house():
    turtle.hideturtle()
    turtle.fillcolor('DeepSkyBlue')

    turtle.begin_fill()

    for i in range(4):
        turtle.forward(160)
        turtle.left(90)

    turtle.end_fill()

    turtle.penup()
    turtle.goto(-40, 160)
    turtle.pendown()
    turtle.fillcolor('chocolate4')
    a = 120
    b = math.sqrt(2 * (a ** 2))
    turtle.begin_fill()
    turtle.forward(a * 2)
    turtle.left(135)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(b)
    turtle.end_fill()
    time.sleep(5)
