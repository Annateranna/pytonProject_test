import numpy as np


def max_index():
    n, m = int(input()), int(input())
    matrix = []
    matrix_temp = []

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)

    max_i = np.max(matrix)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == max_i:
                matrix_temp.append([i, j])
                break
                
    print(matrix_temp[0][0], matrix_temp[0][1])
