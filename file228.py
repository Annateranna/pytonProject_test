def knbys():
    timur, ruslan = input(), input()
    if timur == ruslan:
        print('ничья')
    else:
        list_all = 'кбнСя'
        mod = 5 - abs((list_all.find(timur[0]) - list_all.find(ruslan[0])))
        if mod == 1 or mod == 3:
            if list_all.find(timur[0]) < list_all.find(ruslan[0]):
                print('Тимур')
            else:
                print('Руслан')
        else:
            if list_all.find(timur[0]) > list_all.find(ruslan[0]):
                print('Тимур')
            else:
                print('Руслан')



