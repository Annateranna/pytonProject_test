def ekz():
    dnk = {'A': 'U', 'G': 'C', 'C': 'G', 'T': 'A'}

    s = input()

    for i in range(len(s)):
        print(dnk[s[i]], end='')
