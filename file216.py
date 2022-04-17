def chinese_year():
    year_l = ['2000', 'Дракон', '2001', 'Змея', '2002', 'Лошадь', '2003', 'Овца', '2004', 'Обезьяна', '2005', 'Петух',
              '2006', 'Собака', '2007', 'Свинья', '2008', 'Крыса', '2009', 'Бык', '2010', 'Тигр', '2011', 'Заяц']
    year = int(input())
    i = 0
    flag = False
    while flag is not True:
        if abs(year - int(year_l[i])) % 12 == 0:
            print(year_l[i + 1])
            flag = True
        i += 2
