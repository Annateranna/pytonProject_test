def merge(values):
    d = {}
    for i in range(len(values)):
        for k, v in values[i].items():
            d[k] = d.get(k, set())
            d[k].add(v)
    return d


def ekz():
    result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])

    print(result)

