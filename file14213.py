import turtle
import time


def bear():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(2)
    turtle.circle(120)
    turtle.circle(60)
    turtle.penup()
    turtle.goto(-60, 120)
    turtle.dot(25)
    turtle.goto(60, 120)
    turtle.dot(25)
    turtle.goto(0, 80)
    turtle.pendown()
    turtle.circle(12)
    turtle.penup()
    turtle.goto(0, 80)
    turtle.pendown()
    turtle.left(90)
    turtle.backward(50)
    turtle.penup()
    turtle.goto(-60, 245)
    turtle.pendown()
    turtle.circle(40)
    turtle.penup()
    turtle.goto(142, 245)
    turtle.pendown()
    turtle.circle(40)
    time.sleep(5)

