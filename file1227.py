import random


def pairs():
    n = int(input())
    s = [input() for _ in range(n)]
    temp = []
    i = 0

    while i < n:
        c = random.choice(s)
        if c != s[i] and c not in temp:
            print(s[i], '-', c)
            temp.append(c)
            i += 1
