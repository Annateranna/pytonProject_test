def push():
    list_all = input().split()
    length = len(list_all)
    list_new = [list_all[length - 1]]
    for i in range(1, length):
        list_new.append(list_all[i - 1])
    print(' '.join(list_new))
