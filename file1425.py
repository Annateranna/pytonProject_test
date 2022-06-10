import turtle
import time


def spiral(side):
    turtle.showturtle()
    colors = ['Blue', 'Yellow', 'chartreuse4', 'DarkMagenta', 'DarkGoldenRod1', 'Red']
    for i in range(44):
        turtle.pensize(i)
        turtle.color(colors[i % len(colors)])
        turtle.left(45)
        turtle.forward(side + 5 * i)


def turtle1():
    side = 10
    spiral(side)
    time.sleep(5)
