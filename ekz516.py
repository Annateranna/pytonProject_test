def latin():
    n = int(input())
    matrix = []
    matrix_temp = [[0] * n for _ in range(n)]
    flag = True
    count = 0

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)

    for i in range(n):
        for j in range(1, n + 1):
            if j in matrix[i]:
                flag *= True
                count += 1
            else:
                flag *= False
                break
        if count == n:
            flag *= True
            count = 0
        else:
            flag *= False
            break

    for i in range(n):
        for j in range(n):
            matrix_temp[i][j] = matrix[j][i]

    for i in range(n):
        for j in range(1, n + 1):
            if j in matrix_temp[i]:
                flag *= True
                count += 1
            else:
                flag *= False
                break
        if count == n:
            flag *= True
            count = 0
        else:
            flag *= False
            break

    if flag:
        print('YES')
    else:
        print('NO')
