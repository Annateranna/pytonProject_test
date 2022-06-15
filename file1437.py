import random
import turtle
import math
import time


def anyangles(a, n, x, y, c):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.pendown()
    for _ in range(n):
        turtle.forward(a)
        turtle.right(360 / n)
    turtle.end_fill()
        


def turtle1():
    turtle.Screen().setup(600, 600)
    turtle.speed(0)
    turtle.Screen().colormode(255)
    turtle.hideturtle()
    s = 5000
    x = -280
    y = 280
    for i in range(5):
        for _ in range(5):
            c = (random.randrange(255), random.randrange(255), random.randrange(255))
            n = random.randrange(3, 6)
            a = math.sqrt(s * 4 * math.tan(math.radians(180 / n)) / n)
            anyangles(a, n, x, y, c)
            x += 110
        x = -280
        y -= 110
    time.sleep(5)
