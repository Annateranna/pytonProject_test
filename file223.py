def change():
    list_all = input().split()
    i = 1
    if len(list_all) % 2 == 0:
        while i <= len(list_all):
            list_all[i - 1], list_all[i] = list_all[i], list_all[i - 1]
            i += 2
    else:
        while i < len(list_all):
            list_all[i - 1], list_all[i] = list_all[i], list_all[i - 1]
            i += 2
    print(' '.join(list_all))
    