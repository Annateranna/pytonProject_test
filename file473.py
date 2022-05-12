import numpy as np


def exponentiation():
    n = int(input())
    matrix1 = []

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix1.append(temp)

    e = int(input())

    matrix_temp = np.linalg.matrix_power(matrix1, e)

    for i in range(n):
        for j in range(n):
            print(matrix_temp[i][j], end=' ')
        print()
