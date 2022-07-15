with open('grades.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
    students = [s.split() for s in data]
    good = [g for g in students if int(g[1]) >= 65 and int(g[2]) >= 65 and int(g[3]) >= 65]
    print(len(good))
