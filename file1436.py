import random
import turtle
import time


def star(side, color, x, y):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(36)
    for _ in range(4):
        turtle.forward(side)
        turtle.left(144)
    turtle.forward(side)
    turtle.end_fill()


def turtle1():
    turtle.speed(0)
    turtle.Screen().colormode(255)
    for _ in range(100):
        size = random.randrange(2, 25)
        color = (random.randrange(255), random.randrange(255), random.randrange(255))
        x = random.randrange(-320, 320)
        y = random.randrange(-240, 240)
        star(size, color, x, y)
    time.sleep(5)
