def ekz():
    n = int(input())
    d = {}

    for _ in range(n):
        s = input().split()
        d[s[0]] = d.get(s[0], {})
        if s[1] not in d[s[0]]:
            d[s[0]].update({s[1]: int(s[2])})
        else:
            d[s[0]][s[1]] = d[s[0]].get(s[1]) + int(s[2])

    for k in sorted(d):
        print(k, ':', sep='')
        for k1, v1 in sorted(d[k].items()):
            print(k1, v1)

