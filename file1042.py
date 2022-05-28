def anagram():
    d1 = {}
    d2 = {}
    for key in input():
        d1[key] = d1.get(key, 0) + 1

    for key in input():
        d2[key] = d2.get(key, 0) + 1

    print('YES' if d1 == d2 else 'NO')
