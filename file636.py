def competition():
    n = int(input())
    comp_list = [tuple(input().split()) for _ in range(n)]

    for i in range(n):
        print(' '.join(comp_list[i]))

    print()

    for i in range(n):
        if int(comp_list[i][1]) >= 4:
            print(' '.join(comp_list[i]))

