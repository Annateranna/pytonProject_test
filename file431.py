def list_n():
    n = int(input())
    list_small = [i for i in range(1, n + 1)]
    list_large = [list_small] * n
    for i in range(n):
        print(list_large[i], sep='\n')

