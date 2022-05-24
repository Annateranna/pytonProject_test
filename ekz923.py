def cities():
    n = int(input())
    list_l = [input() for _ in range(n + 1)]

    l_set = set(list_l)

    print("OK" if len(list_l) == len(l_set) else "REPEAT")
