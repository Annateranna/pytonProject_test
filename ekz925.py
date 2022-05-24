def badday():
    s1 = set(input().split())
    s2 = set(input().split())

    if s1 & s2 != set():
        print(*sorted(s1 & s2, key=int, reverse=True))
    else:
        print('BAD DAY')

