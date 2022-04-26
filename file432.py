def list_n():
    n = int(input())
    list_all = [[j for j in range(1, i + 1)] for i in range(1, n + 1)]
    for i in range(n):
        print(list_all[i], sep='\n')
