def sinonim():
    n = int(input())
    dictionary = {}

    for _ in range(n):
        s = input().split()
        dictionary[s[0]] = dictionary.get(s[0], s[1])

    example = input()

    for key, value in dictionary.items():
        if example == key:
            print(value)
        elif example == value:
            print(key)
