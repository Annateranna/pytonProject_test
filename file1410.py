import turtle
import time


def star(side):
    turtle.showturtle()
    turtle.left(36)
    for _ in range(4):
        turtle.forward(side)
        turtle.left(144)
    turtle.forward(side)


def turtle1():
    side = int(input())
    star(side)
    time.sleep(5)
