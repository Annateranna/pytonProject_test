def snowflake():
    n = int(input())
    matrix = [[""] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == n // 2:
                matrix[i][j] = "*"
            elif j == n // 2:
                matrix[i][j] = "*"
            elif i == j:
                matrix[i][j] = "*"
            elif i == n - 1 - j:
                matrix[i][j] = "*"
            else:
                matrix[i][j] = "."

    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()
