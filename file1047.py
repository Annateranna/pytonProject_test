def script():
    enigma, n = [c for c in input()], int(input())
    dictionary = {}
    d_enigma = {}
    l_dictionary = []
    l_enigma = []

    for _ in range(n):
        s = input().split(': ')
        dictionary[s[0]] = dictionary.get(s[0], int(s[1]))

    for e in enigma:
        d_enigma[e] = d_enigma.get(e, 0) + 1

    for key_d, value_d in dictionary.items():
        for key_e, value_e in d_enigma.items():
            if value_d == value_e:
                l_dictionary.append(key_d)
                l_enigma.append(key_e)

    info = dict(zip(l_enigma, l_dictionary))

    for c in enigma:
        print(info[c], end='')
