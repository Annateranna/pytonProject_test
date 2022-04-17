def coordinates():
    n = int(input())
    plane1 = 0
    plane2 = 0
    plane3 = 0
    plane4 = 0
    for i in range(n):
        xy = input().split()
        if int(xy[0]) > 0 and int(xy[1]) > 0:
            plane1 += 1
        elif int(xy[0]) < 0 and int(xy[1]) < 0:
            plane2 += 1
        elif int(xy[0]) < 0 and int(xy[1]) < 0:
            plane3 += 1
        elif int(xy[0]) > 0 and int(xy[1]) < 0:
            plane4 += 1
        xy.clear()
    print('Первая четверть:', plane1)
    print('Вторая четверть:', plane2)
    print('Третья четверть:', plane3)
    print('Четвертая четверть:', plane4)


