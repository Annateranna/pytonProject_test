def chess():
    ch = input().aplit()
    n = int(ch[0])
    m = int(ch[1])
    matrix = [[] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                matrix[i].append(".")
            elif (i + j) % 2 == 1:
                matrix[i].append("*")

    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print()


