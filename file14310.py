import turtle
import time


def planet(r, x, y, color, planet):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(r)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(-20)
    turtle.write(planet, align='center', font=('Verdana', 8, 'normal'))
    turtle.forward(20)
    turtle.right(90)


def turtle1():
    turtle.Screen().setup(800, 300)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    x = -300
    planets = ((80, 'Yellow', 'Солнце'), (15, 'DarkGoldenrod1', 'Меркурий'), (20, 'DarkGoldenrod1', 'Венера'),
               (15, 'aquamarine2', 'Земля'), (12, 'brown1', 'Марс'), (30, 'DarkGoldenrod1', 'Юпитер'),
               (30, 'DarkGoldenrod1', 'Сатурн'), (25, 'cyan3', 'Уран'), (23, 'blue3', 'Нептун'),
               (9, 'DarkGoldenrod1', 'Плутон'))

    for i in range(10):
        y = 40 - planets[i][0]
        planet(planets[i][0], x, y, planets[i][1], planets[i][2])
        if i == 6:
            turtle.penup()
            turtle.right(90)
            turtle.forward(11)
            turtle.left(90)
            turtle.right(45)
            turtle.backward(50)
            turtle.pendown()
            for _ in range(2):
                turtle.circle(50, 90)
                turtle.circle(50 // 6, 90)
            turtle.left(45)
        if i < 9:
            x += planets[i][0] + planets[i + 1][0] / 2 + 30
        else:
            x += planets[i][0] + 30
    time.sleep(5)
