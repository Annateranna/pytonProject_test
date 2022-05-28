def slang():
    n = int(input())
    dictionary = {}

    for _ in range(n):
        s = input().split(': ')
        dictionary[s[0].lower()] = dictionary.get(s[0].lower(), s[1])

    m = int(input())

    for _ in range(m):
        key = input().lower()
        if key in dictionary:
            print(dictionary[key])
        else:
            print('Не найдено')
