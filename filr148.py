import turtle
import time


def rhombus(side, turn):
    turtle.showturtle()
    turtle.left(turn)
    for _ in range(2):
        turtle.forward(side)
        turtle.left(60)
        turtle.forward(side)
        turtle.left(120)


def turtle1():
    side = int(input())
    for _ in range(10):
        rhombus(side, 35)
    time.sleep(5)
