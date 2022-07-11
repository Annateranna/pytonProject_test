ip = input().split('.')
res = list(map(lambda x: True if x.isdigit() and 0 <= int(x) <= 255 else False, ip))
print(all(res))
