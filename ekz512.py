import numpy as np

def hatch_area():
    n = int(input())
    matrix = []

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)

    max_hatch = np.min(matrix)

    for i in range(n):
        for j in range(n):
            if i >= n - 1 - j:
                if matrix[i][j] > max_hatch:
                    max_hatch = matrix[i][j]

    print(max_hatch)
