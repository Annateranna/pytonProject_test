import turtle
import time


def snow_turtle(side, turn):
    turtle.showturtle()
    turtle.left(turn)
    turtle.penup()
    turtle.forward(side - 40)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)
    turtle.stamp()
    turtle.penup()
    turtle.backward(20)
    turtle.pendown()
    turtle.backward(20)
    turtle.penup()
    turtle.backward(side - 40)


def turtle1():
    side = 100
    turtle.shape('turtle')
    turtle.pensize(3)
    for _ in range(12):
        snow_turtle(side, 30)
    turtle.stamp()
    time.sleep(5)
