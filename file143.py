import turtle
import time


def square(side):
    turtle.shape('turtle')
    turtle.showturtle()
    turtle.left(65)
    for _ in range(3):
        turtle.forward(side)
        turtle.left(90)
    turtle.forward(side)


def turtle1():
    side = int(input())
    for _ in range(3):
        square(side)
    time.sleep(5)
