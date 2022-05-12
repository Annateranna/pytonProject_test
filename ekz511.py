def chunked(list_1, n):
    list_all = []
    count = 0
    for i in range(len(list_1)):
        if count < n:
            list_all += [list_1[i::n]]
            count += 1
    print(list_all)


def nelement():
    list_1, n = [c for c in input().split()], int(input())
    chunked(list_1, n)

