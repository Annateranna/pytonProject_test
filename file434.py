from math import factorial


def pascal(n):
    list_small = [int(factorial(n) / (factorial(i) * factorial(n - i))) for i in range(n + 1)]
    return list_small


def list_n(n):
    list_large = [pascal(i) for i in range(n)]
    for i in range(n):
        print(*list_large[i])



