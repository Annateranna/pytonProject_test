from functools import reduce


def evaluate(coefficients, x):
    list_x = []
    for i in range(len(coefficients) - 1, -1, -1):
        list_x.append(x ** i)
    s = list(map(lambda k, p: k * p, coefficients, list_x))
    result = reduce(lambda y, z: y + z, s)
    print(result)


coeffs_input = input().split()
coeffs = [int(c) for c in coeffs_input]
x = int(input())
evaluate(coeffs, x)
