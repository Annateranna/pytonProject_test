def matrix(n=None, m=None, value=None):
    if n is None and m is None and value is None:
        return [[0]]
    elif n is not None and m is None and value is None:
        return [[0] * n for _ in range(n)]
    elif n is not None and m is not None and value is None:
        return [[0] * m for _ in range(n)]
    else:
        return [[value] * m for _ in range(n)]


print(matrix())
print(matrix(5))
print(matrix(5, 6))
print(matrix(5, 6, 1))
