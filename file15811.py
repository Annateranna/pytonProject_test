rgb = input().split()
opposite_rgb = list(map(lambda x: 255 - int(x), rgb))
print(*opposite_rgb)
