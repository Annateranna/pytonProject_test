func = lambda a: True if a[0].lower() == 'a' and a[len(a) - 1].lower() == 'a' else False
print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))