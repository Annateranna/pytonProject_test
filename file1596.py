password = list(input())
print('YES' if all([any(list(map(lambda x: x.isdigit(), password))), any(list(map(lambda x: x.isupper(), password))),
          any(list(map(lambda x: x.islower(), password))), len(password) >= 7]) else 'NO')


