def anagram2():
    def anagram(s1):

        s1 = s1.lower().split()

        for i in range(len(s1)):
            s1[i] = s1[i].strip('.,;:-?!()')

        s1 = ''.join(s1)

        d1 = {}

        for key in s1:
            d1[key] = d1.get(key, 0) + 1

        return d1

    print('YES' if anagram(input()) == anagram(input()) else 'NO')
