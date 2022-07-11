from functools import reduce


def product_of_odds(data):
    res = filter(lambda x: x % 2 == 1, data)
    result = reduce(lambda a, b: a * b, res, 1)
    return result


