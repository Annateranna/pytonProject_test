import turtle
import time


def rhombus(side):
    turtle.showturtle()
    for _ in range(2):
        turtle.forward(side)
        turtle.left(120)
        turtle.forward(side)
        turtle.left(60)
    turtle.forward(side)


def turtle1():
    side = int(input())
    rhombus(side)
    time.sleep(5)
