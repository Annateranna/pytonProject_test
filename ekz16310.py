def gematry(words):
    res = []
    for word in words:
        res += list(map(lambda x: ord(x.upper()) - ord('A'), word))
    return sum(res)


n = int(input())
words = sorted([input() for _ in range(n)])
print(*sorted(words, key=gematry), sep='\n')
