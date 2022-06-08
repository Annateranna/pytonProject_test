import turtle
import time


def hexagon(side, turn):
    turtle.showturtle()
    turtle.left(turn)
    for _ in range(5):
        turtle.forward(side)
        turtle.left(60)
    turtle.forward(side)


def turtle1():
    side = int(input())
    for _ in range(3):
        hexagon(side, 180)
    turtle.backward(side)
    for _ in range(4):
        hexagon(side, 120)
        turtle.backward(side)
    time.sleep(5)
