def correct():
    text = input().split()
    result = {}

    for key in text:
        result[key] = result.get(key, 0) + 1
        if int(result[key]) != 1:
            print(key, '_', int(result[key]) - 1, sep='', end=' ')
        else:
            print(key, end=' ')


