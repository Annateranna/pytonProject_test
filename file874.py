def no_more_than_two():
    s1, s2, s3 = set(input().split()), set(input().split()), set(input().split())
    print(*sorted((s1 | s2 | s3) - (s1 & s2 & s3), key=int))
