with open('goats.txt', 'r', encoding='utf-8') as input_file, open('answer.txt', 'w', encoding='utf-8') as output_file:
    input_file.readline()
    colour = ''
    colours = []
    result = {}
    sorted_colours = []
    while colour.strip() != 'GOATS':
        colour = input_file.readline()
        colours.append(colour.strip())
    colours = colours[:len(colours) - 1]
    goats = input_file.readlines()
    for g in goats:
        result[g.strip()] = result.get(g.strip(), 0) + 1
    for c in colours:
        if result[c] > 7:
            sorted_colours.append(c)
    print(*sorted(sorted_colours), sep='\n', file=output_file)
