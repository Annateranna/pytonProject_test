abscissas, ordinates, applicates = list(map(float, input().split())), list(map(float, input().split())), \
                                   list(map(float, input().split()))
r = 2
coordinates = [abscissas, ordinates, applicates]
result = all(map(lambda x, y, z: x**2 + y**2 + z**2 <= r**2, coordinates[0], coordinates[1], coordinates[2]))
print(result)
