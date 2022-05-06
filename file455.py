def mirror_matrix():
    n = int(input())
    matrix = []

    for i in range(n):
        temp = [ch for ch in input().split()]
        matrix.append(temp)

    for i in range(n):
        matrix[i][i], matrix[n - 1 - i][i] = matrix[n - 1 - i][i], matrix[i][i]

    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()
