def countries_cities():
    n = int(input())
    dictionary = {}

    for _ in range(n):
        s = input().split()
        for i in range(1, len(s)):
            dictionary[s[i]] = dictionary.get(s[i], s[0])

    m = int(input())

    for _ in range(m):
        s = input()
        for key in dictionary.keys():
            if key == s:
                print(dictionary[key])



