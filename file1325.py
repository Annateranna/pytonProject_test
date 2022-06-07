from fractions import Fraction


def row_of_squares():
    n = int(input())
    total = 0

    for i in range(1, n + 1):
        total += Fraction(1, (i ** 2))

    print(total)
