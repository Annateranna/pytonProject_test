def build_query_string(d):
    s = []
    for k, v in d.items():
        s += [k + '=' + str(v)]

    s = sorted(s)
    s1 = '&'.join(s)

    return s1


def ekz():
    print(build_query_string({'name': 'timur', 'age': 28}))
    print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
