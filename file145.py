import turtle
import time


def hexagon(side):
    turtle.showturtle()
    for _ in range(5):
        turtle.forward(side)
        turtle.left(60)
    turtle.forward(side)


def turtle1():
    side = int(input())
    hexagon(side)
    time.sleep(5)
