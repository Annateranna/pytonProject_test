def fill_5():
    ch = input().split()
    n = int(ch[0])
    m = int(ch[1])
    matrix = [[0] * m for _ in range(n)]

    list_l = [j for j in range(1, m + 1)]

    for i in range(n):
        if i <= m:
            matrix[i] = list_l[i:] + list_l[:i]
        else:
            matrix[i] = list_l[i % m:] + list_l[:i]

    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end='')
        print()

