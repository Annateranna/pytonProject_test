def chunked(list_1, n):
    list_all = []
    while n <= len(list_1):
        list_all += [list_1[:n]]
        del list_1[:n]
    if list_1:
        list_all += [list_1]
    print(list_all)


def for_chunked():
    list_1, n = [c for c in input().split()], int(input())
    chunked(list_1, n)

