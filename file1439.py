import turtle
import time


def turtle1():
    turtle.Screen().setup(600, 600)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, -30)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    turtle.goto(0, 0)
    text = ['Восток', 'Север', 'Запад', 'Юг']
    al = ['left', 'center', 'right', 'center']
    for i in range(4):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.forward(90)
        turtle.penup()
        turtle.forward(10)
        turtle.write(text[i], align=al[i])
        turtle.backward(90)
        turtle.left(90)
    time.sleep(5)




