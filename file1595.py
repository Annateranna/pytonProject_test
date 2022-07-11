a, b = input(), input()
result = []
for i in range(int(a), int(b)):
    str_i = str(i)
    list_i = [str_i for _ in range(len(str_i))]
    res = list(map(lambda x, y: True if int(y) != 0 and int(x) % int(y) == 0 else False, list_i, list(str_i)))
    if all(res):
        result.append(str_i)
print(*result)
