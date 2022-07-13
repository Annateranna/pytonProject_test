def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as file:
        keys = [key.strip() for key in file.readline().split(',')]
        data = file.readlines()
        dictionary = []

        for line in data:
            line = line.strip()
            value = line.split(',')
            dictionary.append(dict(zip(keys, value)))

        return dictionary


