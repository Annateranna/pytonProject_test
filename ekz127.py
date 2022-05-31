def ekz():
    d = {'write': 'W', 'read': 'R', 'execute': 'X'}
    n = int(input())
    files = {}

    for _ in range(n):
        s = input().split()
        files[s[0]] = files.get(s[0], s[1:])

    m = int(input())

    for _ in range(m):
        s = input().split()
        if d[s[0]] in files[s[1]]:
            print('OK')
        else:
            print('Access denied')

