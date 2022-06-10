import turtle
import time


def olimpic():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(7)
    turtle.circle(70)
    turtle.penup()
    turtle.goto(-147, 0)
    turtle.color('DeepSkyBlue')
    turtle.pendown()
    turtle.circle(70)
    turtle.penup()
    turtle.goto(147, 0)
    turtle.color('Red')
    turtle.pendown()
    turtle.circle(70)
    turtle.penup()
    turtle.goto(-73.5, -70)
    turtle.color('Yellow')
    turtle.pendown()
    turtle.circle(70)
    turtle.penup()
    turtle.goto(73.5, -70)
    turtle.color('lawngreen')
    turtle.pendown()
    turtle.circle(70)
    time.sleep(5)

