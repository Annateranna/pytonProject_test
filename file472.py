def multiply2():
    ch = input().split()
    n = int(ch[0])
    m = int(ch[1])
    matrix1 = []
    matrix2 = []

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix1.append(temp)

    _ = input()

    ch = input().split()
    k = int(ch[1])

    matrix_temp = [[0] * n for _ in range(k)]

    for i in range(m):
        temp = [int(num) for num in input().split()]
        matrix2.append(temp)

    for i in range(n):
        for j in range(k):
            for p in range(m):
                matrix_temp[i][j] += matrix1[i][p] * matrix2[p][j]

    for i in range(n):
        for j in range(k):
            print(matrix_temp[i][j], end=' ')
        print()

