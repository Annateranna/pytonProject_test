def fill_2():
    ch = input().split()
    n = int(ch[0])
    m = int(ch[1])
    matrix = [[0] * n for _ in range(m)]
    count = 0

    for i in range(m):
        for j in range(n):
            count += 1
            matrix[i][j] += count

    for i in range(n):
        for j in range(m):
            print(str(matrix[j][i]).ljust(3), end=' ')
        print()

