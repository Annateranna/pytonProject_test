import random
import turtle
import time


def snowflake(size, color, x, y):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.pendown()
    small = size / 3
    turtle.dot(5)
    for _ in range(8):
        turtle.left(360 / 8)
        turtle.forward(size)
        turtle.backward(size)
        for _ in range(3):
            turtle.forward(small)
            turtle.right(45)
            turtle.forward(small)
            turtle.backward(small)
            turtle.left(90)
            turtle.forward(small)
            turtle.backward(small)
            turtle.right(45)
            turtle.forward(small)
            turtle.backward(small)
        turtle.backward(size)


def turtle1():
    turtle.speed(0)
    turtle.Screen().colormode(255)
    turtle.Screen().bgcolor('cyan')
    for _ in range(random.randrange(1, 20)):
        turtle.pensize(random.randrange(10))
        size = random.randrange(20, 100)
        color = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
        x = random.randrange(-320, 320)
        y = random.randrange(-240, 240)
        snowflake(size, color, x, y)
    time.sleep(5)
