def is_larger():
    list_dig = input().split()
    count = 0
    for i in range(1, len(list_dig)):
        if int(list_dig[i]) > int(list_dig[i - 1]):
            count += 1
    print(count)
