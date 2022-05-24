def online5():
    m = int(input())
    n = int(input())
    s = set(input() for _ in range(n))

    for _ in range(m - 1):
        n = int(input())
        temp = set(input() for _ in range(n))
        s = s & temp
        temp.clear()

    print(*sorted(s), sep='\n')



