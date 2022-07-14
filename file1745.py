with open('class_scores.txt', 'r', encoding='utf-8') as input_file, open('new_scores.txt', 'w', encoding='utf-8') as output_file:
    lines = input_file.readlines()
    for line in lines:
        l = line.split()
        if int(l[1]) < 96:
            print(l[0], int(l[1]) + 5, file=output_file)
        else:
            print(l[0], 100, file=output_file)
