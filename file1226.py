import random


def bingo():
    s = set()
    while len(s) < 25:
        s |= {(random.randrange(1, 76))}

    matrix = [[0] * 5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            matrix[i][j] = s.pop()

    matrix[2][2] = 0

    for r in range(5):
        for c in range(5):
            print(str(matrix[r][c]).ljust(3), end=' ')
        print()
