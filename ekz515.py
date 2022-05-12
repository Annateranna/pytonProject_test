def simmetrical():
    n = int(input())
    matrix = []
    flag = True

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == matrix[n - 1 - j][n - 1 - i]:
                flag = True
            else:
                flag = False

    if flag:
        print('YES')
    else:
        print('NO')
