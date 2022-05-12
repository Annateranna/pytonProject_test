def multiply():
    ch = input().split()
    n = int(ch[0])
    m = int(ch[1])
    matrix1 = []
    matrix2 = []

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix1.append(temp)

    _ = input()

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix2.append(temp)

    for i in range(n):
        for j in range(m):
            print(matrix1[i][j] + matrix2[i][j], end=' ')
        print()
