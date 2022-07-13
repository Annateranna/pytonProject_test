with open('file.txt', 'r', encoding='utf-8') as file:
    data_list = file.readlines()
    file.seek(0)
    data = file.read()
    letters = 0
    for c in data:
        if c.isalpha():
            letters += 1
    words = data.split()
    print(f'Input file contains:\n{letters} letters\n{len(words)} words\n{len(data_list)} lines')
