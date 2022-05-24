def online3():
    s1 = set(input().split())
    s2 = set(input().split())

    print(*sorted(s1 | s2))
