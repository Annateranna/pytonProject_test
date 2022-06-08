import turtle
import time


def rectangle(width, height):
    turtle.shape('turtle')
    turtle.showturtle()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    time.sleep(5)


def turtle1():
    w, h = int(input()), int(input())
    rectangle(w, h)
