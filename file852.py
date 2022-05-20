def unicum2():
    list_l = []

    for i in range(int(input())):
        list_l += input().lower().split()

    string = ''.join(list_l)

    print(len(set(string)))
