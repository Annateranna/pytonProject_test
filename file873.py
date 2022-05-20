def three_students():
    s1, s2, s3 = set(input().split()), set(input().split()), set(input().split())
    print(*sorted(s1 & s2 - s3, key=int, reverse=True))
