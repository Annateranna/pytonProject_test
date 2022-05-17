def threebonacci():
    n = int(input())
    th1, th2, th3 = 1, 1, 1
    print(th1, end=' ')
    for i in range(n - 1):
        print(th1, end=' ')
        th1, th2, th3 = th3, th1, th1 + th2 + th3

