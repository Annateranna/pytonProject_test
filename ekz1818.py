name = input()

with open(name, 'r', encoding='utf-8') as file:
    lines = [lines.strip('\n') for lines in file.readlines()]
    l = [l for l in lines if l != '']
    flag = True
    for i in range(len(l)):
        if l[i][0:3] == 'def' and l[i - 1][0] != '#':
            print(l[i][4:l[i].index('(')])
            flag = False

    if flag:
        print('Best Programming Team')

