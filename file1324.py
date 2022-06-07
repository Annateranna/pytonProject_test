from fractions import Fraction


def operation():
    a1 = input()
    b1 = input()
    a = Fraction(a1)
    b = Fraction(b1)
    print(a1, '+', b1, '=', a + b)
    print(a1, '-', b1, '=', a - b)
    print(a1, '*', b1, '=', a * b)
    print(a1, '/', b1, '=', a / b)
