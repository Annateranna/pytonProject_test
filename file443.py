def trace_matrix():
    n = int(input())
    matrix = []
    trace = 0

    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)

    for i in range(n):
        trace += matrix[i][i]

    print(trace)
