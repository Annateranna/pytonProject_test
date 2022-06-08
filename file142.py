import turtle
import time


def triangle(side):
    turtle.shape('turtle')
    turtle.showturtle()
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    time.sleep(5)


def turtle1():
    side = int(input())
    triangle(side)
