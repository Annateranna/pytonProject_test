def compare():
    s1, s2 = input(), input()
    example = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    print('YES' if set(s1 + s2) == example else 'NO')
