import random


with open('first_names.txt', 'r', encoding='utf-8') as first, open('last_names.txt', 'r', encoding='utf-8') as last:
    first_names = first.read().split()
    last_names = last.read().split()

    for _ in range(3):
        print(first_names[random.randrange(len(first_names))], last_names[random.randrange(len(last_names))])
