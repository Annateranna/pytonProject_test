def diagonal():
    ch = input().split()
    n = int(ch[0])
    m = int(ch[1])
    matrix = [[0] * m for _ in range(n)]
    count = 0

    for k in range(n + m - 1):
        for i in range(n):
            for j in range(m):
                if i + j == k:
                    count += 1
                    matrix[i][j] = count

    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end='')
        print()

