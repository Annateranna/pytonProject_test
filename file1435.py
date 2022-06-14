import turtle


def turtle1():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.Screen().bgcolor('blue4')
    turtle.penup()
    turtle.color('DarkGoldenrod1')
    turtle.dot(200, 'DarkGoldenrod1')
    moon = turtle.Turtle()
    moon.hideturtle()
    moon.pensize(200)
    moon.pencolor('blue4')
    moon.penup()
    while True:
        for i in range(-201, 401):
            moon.goto(-i, 0)
            moon.dot()
            turtle.tracer(7, 0)
            turtle.hideturtle()
            moon.clear()

