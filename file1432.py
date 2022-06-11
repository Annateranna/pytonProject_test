import turtle
import time


def light(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(24)
    turtle.end_fill()


def turtle1():
    color = ['chartreuse2', 'Yellow', 'Red']
    turtle.hideturtle()
    turtle.speed(0)
    turtle.fillcolor('Black')
    turtle.begin_fill()
    turtle.forward(78)
    turtle.left(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(78)
    turtle.left(90)
    turtle.forward(180)
    turtle.end_fill()
    x = 15
    y = 8
    for i in range(3):
        turtle.penup()
        turtle.goto(x, 36 + 56 * i)
        turtle.pendown()
        light(color[i])
    time.sleep(5)
