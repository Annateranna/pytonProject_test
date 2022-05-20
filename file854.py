def unicum_num():
    list_l = input().split()

    for i in range(len(list_l)):
        list_l[i] = list_l[i].lstrip('0')

    set_s = set(list_l)

    for i in list_l:
        if i in set_s:
            set_s.remove(i)
            print('NO')
        else:
            print('YES')
