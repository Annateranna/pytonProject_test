from fractions import Fraction
import math


def sorted_fractions():
    n = int(input())
    g = set()

    for i in range(1, n):
        for j in range(1, n + 1):
            if math.gcd(i, j) == 1 and Fraction(i, j) < 1:
                g |= {Fraction(i, j)}

    print(*sorted(g), sep='\n')
