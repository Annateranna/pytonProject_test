from fractions import Fraction
import math


def young_mathematist():
    n = int(input())
    g = 0

    for i in range(n):
        for j in range(n):
            if i + j == n and i < j and math.gcd(i, j) == 1:
                if Fraction(i, j) > g:
                    m = i
                    k = j
                    g = Fraction(i, j)

    print(Fraction(m, k))
