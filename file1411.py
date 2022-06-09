import turtle
import time


def squares(side):
    turtle.showturtle()
    for _ in range(4):
        turtle.backward(side)
        turtle.right(90)


def turtle1():
    side = 30
    for _ in range(31):
        squares(side)
        side += 10
    time.sleep(5)
