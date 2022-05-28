def script():
    enigma, n = [c for c in input()], int(input())
    dictionary = {}
    d_enigma = {}

    for _ in range(n):
        s = input().split(': ')
        dictionary[int(s[1])] = dictionary.get(int(s[1]), s[0])

    for e in enigma:
        d_enigma[e] = d_enigma.get(e, 0) + 1

    new_enigma = {v: k for k, v in d_enigma.items()}

    for c in enigma:
        for key, value in new_enigma.items():
            if c == value:
                print(dictionary[key], end='')
