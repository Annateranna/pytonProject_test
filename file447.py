def sum_4():
    n = int(input())
    matrix = []
    matrix_temp = []

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)

    for i in range(n):
        for j in range(n):
            if (i > j) and (i < n - 1 - j):
                matrix_temp.append(matrix[i][j])

    sum4 = sum(matrix_temp)
    matrix_temp = []

    for i in range(n):
        for j in range(n):
            if (i < j) and (i > n - 1 - j):
                matrix_temp.append(matrix[i][j])

    sum2 = sum(matrix_temp)
    matrix_temp = []

    for i in range(n):
        for j in range(n):
            if (i < j) and (i < n - 1 - j):
                matrix_temp.append(matrix[i][j])

    sum1 = sum(matrix_temp)
    matrix_temp = []

    for i in range(n):
        for j in range(n):
            if (i > j) and (i > n - 1 - j):
                matrix_temp.append(matrix[i][j])

    sum3 = sum(matrix_temp)

    print(f'Верхняя четверть: {sum1}\nПравая четверть: {sum2}\nНижняя четверть: {sum3}\nЛевая четверть: {sum4}')

