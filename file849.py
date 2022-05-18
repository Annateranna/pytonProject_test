def compare():
    list_l = input().split()
    print('YES' if set(list_l[0]) == set(list_l[1]) == set(list_l[2]) else 'NO')
