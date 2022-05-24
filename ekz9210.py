def online4():
    m, n = int(input()), int(input())
    s = set(input() for _ in range(m + n))

    print(m + n - (m + n - len(s)) * 2 or 'NO')
