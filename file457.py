def turn_matrix():
    n = int(input())
    matrix = []

    for i in range(n):
        temp = [ch for ch in input().split()]
        matrix.append(temp)

    for i in range(n):
        for j in range(n):
            print(matrix[n - 1 - j][i], end=' ')
        print()
