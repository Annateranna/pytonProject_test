def matrix1():
    n, m = int(input()), int(input())
    matrix = []
    for i in range(n):
        for j in range(m):
            matrix.append(input())
        print(' '.join(matrix))
        matrix.clear()


