import numpy as np


def max_in_two_area():
    n = int(input())
    matrix = []

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)

    max_hatch = np.min(matrix)

    if n % 2 == 1:
        length = n + 1
    else:
        length = n

    for i in range(int(length / 2)):
        for j in range(i + 1):
            if matrix[i][j] > max_hatch:
                max_hatch = matrix[i][j]

    for i in range(int(length / 2), n):
        for j in range(int(length / 2) - 1):
            if matrix[i][j] > max_hatch:
                max_hatch = matrix[i][j]

    for i in range(int(length / 2)):
        for j in range(n - 1, int(length / 2) - 1, -1):
            if matrix[i][j] > max_hatch:
                max_hatch = matrix[i][j]

    for i in range(int(length / 2), n):
        for j in range(i, n):
            if matrix[i][j] > max_hatch:
                max_hatch = matrix[i][j]

    print(max_hatch)
