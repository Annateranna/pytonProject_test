def matrix1():
    n, m = int(input()), int(input())
    matrix = [[''] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            matrix[i][j] += input()

    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print()

    print()
    
    for i in range(m):
        for j in range(n):
            print(matrix[j][i], end=' ')
        print()
