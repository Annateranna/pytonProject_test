import turtle
import time


def snow(side, turn):
    turtle.showturtle()
    turtle.left(turn)
    turtle.forward(side)
    turtle.stamp()
    turtle.backward(side)


def turtle1():
    side = 100
    n = int(input())
    turtle.shape('triangle')
    for _ in range(n):
        snow(side, 360 / n)
    turtle.dot(20)
    time.sleep(5)
