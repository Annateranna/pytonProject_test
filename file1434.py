import turtle
import time


def circles(side, color):
    turtle.hideturtle()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(0, -side)
    turtle.pendown()
    turtle.circle(side)
    turtle.end_fill()


def turtle1():
    turtle.speed(0)
    color = ['Red', 'Orange', 'Yellow', 'chartreuse2', 'aquamarine', 'cyan', 'CornflowerBlue', 'blue', 'DarkViolet', 'DeepPink' ]
    for i in range(len(color)):
        circles(200 - 20 * i, color[i])
    time.sleep(5)

