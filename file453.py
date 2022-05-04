def exchange():
    n, m = int(input()), int(input())
    matrix = []
    matrix_inv = [[''] * n for _ in range(m)]

    for i in range(n):
        temp = [ch for ch in input().split()]
        matrix.append(temp)

    [k, l] = [int(num) for num in input().split()]

    for j in range(m):
        for i in range(n):
            matrix_inv[j][i] += matrix[i][j]

    matrix_inv[k], matrix_inv[l] = matrix_inv[l], matrix_inv[k]

    for j in range(n):
        for i in range(m):
            print(matrix_inv[i][j], end=' ')
        print()

