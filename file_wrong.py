def knb():
    timur, ruslan = input(), input()
    if timur == ruslan:
        print('ничья')
    else:
        list_all = 'камень ножницы бумага'
        print(list_all.find(timur))
        print(list_all.find(ruslan))
        print(list_all.find(timur) - list_all.find(ruslan))
        if abs(list_all.find(timur) - list_all.find(ruslan)) == (7 or 8):
            if list_all.find(timur) < list_all.find(ruslan):
                print('Тимур')
            else:
                print('Руслан')
        else:
            if list_all.find(timur) > list_all.find(ruslan):
                print('Тимур')
            else:
                print('Руслан')

