with open('data.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
    for line in data[::-1]:
        print(line.strip())
