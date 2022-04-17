def vice_versa():
    num = input()
    if len(num) == 6:
        c = num[0] + num[6:0:-1]
    else:
        n = num.rstrip('0')
        c = n[::-1]
    print(c)


