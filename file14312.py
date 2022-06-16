import turtle
import random
import time


def rectangle(h, w, c):
    turtle.penup()
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.pencolor(c)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
    turtle.end_fill()


def stars(s, c, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.pencolor(c)
    turtle.pendown()
    turtle.circle(s)
    turtle.end_fill()


def turtle1():
    turtle.Screen().setup(400, 400)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.Screen().bgcolor('MidnightBlue')
    turtle.penup()
    for _ in range(50):
        stars(random.randint(1, 2), 'Yellow', random.randint(-190, 190), random.randint(-40, 190))
    turtle.penup()
    turtle.goto(-200, -200)
    sizes = ((150, 55), (200, 60), (340, 95), (175, 55), (300, 65), (205, 35), (155, 35))
    for i in range(7):
        rectangle(sizes[i][0], sizes[i][1], 'RoyalBlue4')
        turtle.forward(sizes[i][1])
    coors = ((-137, -30), (-76, 107), (-76, 88), (-55, -65), (-14, 25), (75, 20))
    for i in range(6):
        turtle.penup()
        turtle.goto(coors[i][0], coors[i][1])

        rectangle(15, 15, 'yellow')

    time.sleep(10)
