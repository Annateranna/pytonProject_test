from math import factorial


def pascal(n):
    list_small = [int(factorial(n) / (factorial(i) * factorial(n - i))) for i in range(0, n + 1)]
    print(list_small)
