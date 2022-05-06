def mirror_matrix():
    n = int(input())
    matrix = []

    for i in range(n):
        temp = [ch for ch in input().split()]
        matrix.append(temp)

    for i in range(int(n/2)):
        for j in range(n):
            matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]

    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()

