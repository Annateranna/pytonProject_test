import turtle
import time


def chess(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    for _ in range(4):
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()


def turtle1():
    turtle.Screen().setup(600, 600)
    turtle.speed(0)
    turtle.hideturtle()
    x = 0
    y = 0
    color = 'Black'
    for i in range(1, 6):
        for j in range(1, 6):
            if (i + j) % 2 == 0:
                color = 'Black'
            elif (i + j) % 2 == 1:
                color = 'white'
            chess(x, y, color)
            x += 20
        y += 20
        x = 0
    time.sleep(5)




    time.sleep(5)



