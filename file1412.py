import turtle
import time


def pattern(side, turn):
    turtle.showturtle()
    for i in range(turn):
        turtle.left(90)
        turtle.forward(side + i * 1.2 * side)


def turtle1():
    side = 5
    turn = 49
    pattern(side, turn)
    time.sleep(5)
