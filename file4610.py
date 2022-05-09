def spiral():
    ch = input().split()
    n = int(ch[0])
    m = int(ch[1])
    matrix = [[0] * m for _ in range(n)]
    count = 0

    for k in range(n):
        for j in range(k, m - k):
            if count < n * m:
                count += 1
                matrix[k][j] = count

        for i in range(k + 1, n - k):
            if count < n * m:
                count += 1
                matrix[i][m - k - 1] = count

        for j in range(k + 1, m - k):
            if count < n * m:
                count += 1
                matrix[n - k - 1][m - j - 1] = count

        for i in range(k + 1, n - 1 - k):
            if count < n * m:
                count += 1
                matrix[n - i - 1][k] = count

    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end='')
        print()

