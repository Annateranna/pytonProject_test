def count_equal():
    list_all = input().split()
    count = 1
    for i in range(1, len(list_all)):
        if int(list_all[i - 1]) < int(list_all[i]):
            count += 1
    print(count)
            