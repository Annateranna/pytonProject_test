def list_list():
    list_1 = [c for c in input().split()]
    list_all = [[]]
    for i in range(len(list_1)):
        for j in range(len(list_1)):
            if j < i + 1:
                list_all += [list_1[j:i + 1]]
    print(sorted(list_all, key=len))

