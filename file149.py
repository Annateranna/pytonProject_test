import turtle
import time


def snow(side, turn):
    turtle.showturtle()
    turtle.color('Yellow')
    turtle.left(turn)
    turtle.forward(side)
    turtle.backward(side)


def turtle1():
    side = int(input())
    for _ in range(12):
        snow(side, 30)
    time.sleep(5)
