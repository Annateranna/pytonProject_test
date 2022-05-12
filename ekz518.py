def parallel():
    n = int(input())
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j + k or j == i + k:
                    matrix[i][j] = k

    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()
