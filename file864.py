def common():
    n = int(input())
    s1 = set(input())

    for i in range(n - 1):
        s2 = set(input())
        s1.intersection_update(s2)

    print(*sorted(s1))

