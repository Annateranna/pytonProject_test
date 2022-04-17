def knb():
    timur, ruslan = input(), input()
    if timur == ruslan:
        print('ничья')
    else:
        list_all = 'кнб'
        if abs(list_all.find(timur[0]) - list_all.find(ruslan[0])) == 1:
            if list_all.find(timur[0]) < list_all.find(ruslan[0]):
                print('Тимур')
            else:
                print('Руслан')
        else:
            if list_all.find(timur[0]) > list_all.find(ruslan[0]):
                print('Тимур')
            else:
                print('Руслан')
