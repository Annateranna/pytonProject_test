def usa_digits():
    n = input()
    s = n[::-1]
    i = 6
    j = 3
    s1 = s[:3]
    if len(n) < 4:
        print(n)
    else:
        while i < len(n) + 3:
            s1 += ',' + s[j:i]
            j = i
            i += 3
        s = s1[::-1]
        print(s)

