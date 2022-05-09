def additional():
    n = int(input())
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == n - 1 - j:
                matrix[i][j] += 1
            elif i < n - 1 - j:
                matrix[i][j] += 0
            elif i > n - 1 - j:
                matrix[i][j] += 2

    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()

