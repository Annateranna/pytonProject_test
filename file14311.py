import turtle
import time


def octagon(a, c):
    turtle.penup()
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.pendown()
    for _ in range(8):
        turtle.forward(a)
        turtle.right(360 / 8)
    turtle.end_fill()


def turtle1():
    turtle.Screen().setup(600, 600)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pensize(5)
    octagon(110, 'White')
    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(12)
    turtle.left(90)
    turtle.pencolor('Red')
    octagon(100, 'Red')
    turtle.pencolor('White')
    turtle.penup()
    turtle.left(90)
    turtle.backward(165)
    turtle.left(90)
    turtle.backward(52)
    turtle.write('STOP', align='center', font=('Arial', 60, 'normal'))
    time.sleep(5)
