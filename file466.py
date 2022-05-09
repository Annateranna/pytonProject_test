def fill_4():
    n = int(input())
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i < n - 1 - j and i < j:
                matrix[i][j] += 1
            elif i > n - 1 - j and i > j:
                matrix[i][j] += 1
            elif i == n - 1 - j:
                matrix[i][j] += 1
            elif i == j:
                matrix[i][j] += 1

    for i in range(n):
        for j in range(n):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()
