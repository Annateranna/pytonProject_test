import turtle
import time


def square(side, turn):         # второй параметр задает поворот
    turtle.showturtle()
    turtle.left(turn)
    for _ in range(3):
        turtle.forward(side)
        turtle.left(90)
    turtle.forward(side)


def turtle1():
    side = int(input())
    for _ in range(4):
        square(side, 0)
    square(side, 45)            # повернули квадраты, рисуем дальше
    for _ in range(3):
        square(side, 0)
    time.sleep(5)
