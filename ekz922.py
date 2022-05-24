def voshod():
    s = input().split()
    s_set = set(s)
    print(len(s) - len(s_set))