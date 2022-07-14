with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
    lines = input_file.readlines()
    outs = enumerate(lines, 1)
    for out in outs:
        print(out[0], ')', ' ', out[1], sep='', file=output_file, end='')

