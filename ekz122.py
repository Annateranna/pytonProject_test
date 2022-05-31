def ekz():
    text = input().split()

    result = {}

    for c in text:
        result[c] = result.get(c, 0) + 1
        print(result[c], end=' ')

