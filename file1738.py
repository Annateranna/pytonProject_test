with open('population.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
    for line in data:
        c = line.split('\t')
        if int(c[1]) > 500000 and c[0][0] == 'G':
            print(c[0])
