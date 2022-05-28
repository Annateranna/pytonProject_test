def phonebook():
    n = int(input())
    dictionary = {}
    count = 0

    for _ in range(n):
        s = input().split()
        dictionary[s[1].lower()] = dictionary.get(s[1].lower(), []) + [s[0]]

    m = int(input())

    for _ in range(m):
        key = input().lower()
        print(*dictionary.get(key, ['абонент не найден']))


