def magic_square():
    n = int(input())
    matrix = []
    ethalon = 0
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0
    sum_4 = 0
    count = 0
    flag = False

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)

    print(matrix)

    for i in range(n):
        ethalon += matrix[i][0]

    for i in range(n):
        for j in range(n):
            sum_1 += matrix[i][j]
            sum_2 += matrix[i][j]
        sum_3 += matrix[i][i]
        sum_4 += matrix[n - 1 - i][n - 1 - i]
        if sum_1 == ethalon and sum_2 == ethalon and sum_3 == ethalon and sum_4 == ethalon:
            flag = True
        sum_1 = 0
        sum_2 = 0

    for i in range(n):
        for j in range(1, n**2 + 1):
            if j in matrix[i]:
                count += 1

    if count == n**2:
        flag = flag and True
    else:
        flag = flag and False

    if flag:
        print('YES')
    else:
        print('NO')
            