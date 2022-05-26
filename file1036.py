def rare_word():
    text = input().lower().split()

    for i in range(len(text)):
        text[i] = text[i].strip('.,;:-?!()')

    result = {}
    result_min = []

    for c in text:
        result[c] = result.get(c, 0) + 1

    max_word = min(result.values())

    for item in result.items():
        if item[1] == max_word:
            result_min += [''.join(item[0])]

    print(sorted(result_min)[0])
