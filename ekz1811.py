name = input()

with open(name, 'r', encoding='utf-8') as file:
    print(len(file.readlines()))
