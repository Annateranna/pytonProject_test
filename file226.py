def multiplication():
    n = int(input())
    list_all = [input() for _ in range(n)]
    result = int(input())
    flag = True
    for i in range(n):
        for j in range(i + 1, n):
            if int(list_all[i]) * int(list_all[j]) == result:
                flag = False
                break
    if not flag:
        print('ДА')
    else:
        print('НЕТ')
