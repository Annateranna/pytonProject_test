import math


def joseph():
    n, k = int(input()), int(input())
    list_all = []
    if n == 1:
        winner = 1
    else:
        for i in range(1, n + 1):
            list_all.append(str(i))
        while len(list_all) > 1:
            list_help = list_all
            for i in range(k - 1):
                list_help = list_all[1:] + list_all[:1]
                list_all = list_help
            list_all = list_help[1:]
        winner = ''.join(list_all)
    print(winner)

