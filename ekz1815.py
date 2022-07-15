name = input()

with open(name, 'r', encoding='utf-8') as file:
    lines = [lines.strip('\n') for lines in file.readlines()]
    if len(lines) <= 10:
        print(*lines, sep='\n')
    else:
        print(*lines[-10:], sep='\n')
