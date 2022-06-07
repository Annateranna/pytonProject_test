from fractions import Fraction
import math


def row_of_eq():
    n = int(input())
    total = 0

    for i in range(1, n + 1):
        total += Fraction(1, math.factorial(i))

    print(total)
