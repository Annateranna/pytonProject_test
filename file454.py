def compare_matrix():
    n = int(input())
    matrix = []
    matrix_inv = [[''] * n for _ in range(n)]

    for i in range(n):
        temp = [ch for ch in input().split()]
        matrix.append(temp)

    for i in range(n):
        for j in range(n):
            matrix_inv[j][i] = matrix[i][j]

    if matrix == matrix_inv:
        print('YES')
    else:
        print('NO')
