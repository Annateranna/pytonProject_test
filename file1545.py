import math


def func_square(x):
    return x**2


def func_cube(x):
    return x**3


def func_sqrt(x):
    return math.sqrt(x)


def func_abs(x):
    return abs(x)


def func_sin(x):
    return math.sin(x)


x, func = int(input()), input()
names = {'квадрат': func_square, 'куб': func_cube, 'корень': func_sqrt, 'модуль': func_abs, 'синус': func_sin}
print(names[func](x))

