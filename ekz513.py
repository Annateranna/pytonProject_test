def transp():
    n = int(input())
    matrix = []

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)

    for i in range(n):
        for j in range(n):
            print(matrix[j][i], end=' ')
        print()
