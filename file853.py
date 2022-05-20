def count_words():
    list_l = input().lower().split()

    for i in range(len(list_l)):
        list_l[i] = list_l[i].strip('.,;:-?!')

    print(len(set(list_l)))
