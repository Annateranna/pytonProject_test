def bigger_than_average():
    n = int(input())
    matrix = []
    average = ['' for _ in range(n)]
    count = 0

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
        total_i = sum(matrix[i])
        average[i] = total_i / n

    for i in range(n):
        for j in range(n):
            if matrix[i][j] > average[i]:
                count += 1
        print(count)
        count = 0
