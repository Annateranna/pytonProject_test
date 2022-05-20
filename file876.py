def noneno():
    s1, s2, s3 = set(input().split()), set(input().split()), set(input().split())
    example = set(str(i) for i in range(11))
    print(*sorted(example - s1 - s2 - s3, key=int))
