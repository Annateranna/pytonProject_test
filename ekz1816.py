name = input()

with open(name, 'r', encoding='utf-8') as file, open('forbidden_words.txt', 'r', encoding='utf-8') as forbidden:
    lines = file.read()
    lines_copy = lines.lower()
    xlines = forbidden.read().split()

    for x in xlines:
        if x.lower() in lines_copy:
            lines_copy = lines_copy.replace(x, '*' * len(x))

    for i in range(len(lines_copy)):
        if lines_copy[i] == '*':
            print('*', end='')
        else:
            print(lines[i], end='')
