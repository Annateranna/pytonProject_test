import turtle
import time


def rays():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-300, -150)
    x = turtle.xcor()
    y = turtle.ycor()
    for i in range(10):
        turtle.pendown()
        turtle.color('aquamarine3')
        turtle.goto(0, 200)
        turtle.penup()
        turtle.goto(x, y)
        turtle.color('blue')
        turtle.dot(5)
        turtle.forward(70)
        x = turtle.xcor()
        y = turtle.ycor()
    turtle.color('red')
    turtle.goto(0, 200)
    turtle.dot(5)


def turtle1():
    turtle.speed(0)
    rays()
    time.sleep(5)
