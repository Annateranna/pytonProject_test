countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

info = list(zip(countries, capitals, population))

for i in range(len(info)):
    print(f'{info[i][1]} is the capital of {info[i][0]}, population equal {info[i][2]} people.')


