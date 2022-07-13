with open('numbers.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
    for line in data:
        numbers = line.split()
        total = sum(map(int, numbers))
        print(total)
