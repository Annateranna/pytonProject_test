with open('lines.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
    max_lines = []
    max_line = max(data, key=len)
    len_max = len(max_line)
    for lines in data:
        if len(lines) == len_max:
            max_lines += [lines.strip()]

    print(*max_lines, sep='\n')
