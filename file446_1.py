import numpy as np


def max_in_two_area():
    n = int(input())
    matrix = []
    matrix_temp = []

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)

    for i in range(n):
        for j in range(n):
            if ((i >= j) and (i <= n - 1 - j)) or ((i <= j) and (i >= n - 1 - j)):
                matrix_temp.append(matrix[i][j])

    max_hatch = np.max(matrix_temp)

    print(max_hatch)
