def same_in_one():
    list_1 = [c for c in input().split()]
    list_all = [[list_1[0]]]
    for i in range(1, len(list_1)):
        if list_1[i] != list_1[i - 1]:
            list_all += [[list_1[i]]]
        else:
            list_all[-1] += [list_1[i]]
        print('1', list_all)
    print(list_all)
