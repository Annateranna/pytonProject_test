def snake():
    ch = input().split()
    n = int(ch[0])
    m = int(ch[1])
    matrix = [[0] * m for _ in range(n)]

    list_l = [num for num in range(1, n * m + 1)]
    
    for i in range(n):
        if i % 2 == 0:
            matrix[i] = list_l[i * m:m * (i + 1)]
        elif i % 2 == 1:
            matrix[i] = list_l[m * (i + 1) - 1:i * m - 1:-1]

    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end='')
        print()

