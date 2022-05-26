def count_s():
    s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange ' \
        'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry ' \
        'apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana ' \
        'melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry ' \
        'apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit ' \
        'banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

    text = s.split()
    result = {}
    result_max = []

    for c in text:
        result[c] = result.get(c, 0) + 1

    max_word = max(result.values())

    for item in result.items():
        if item[1] == max_word:
            result_max += [''.join(item[0])]

    print(sorted(result_max)[0])

