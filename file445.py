def hatch_area():
    n = int(input())
    matrix = []

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)

    max_hatch = max(matrix)

    for i in range(n):
        for j in range(i + 1):
            if matrix[i][j] > max_hatch[0]:
                max_hatch[0] = matrix[i][j]

    print(max_hatch[0])


