def third():
    s1, s2, s3 = set(input().split()), set(input().split()), set(input().split())
    print(*sorted(s3 - s1 - s2, key=int, reverse=True))
