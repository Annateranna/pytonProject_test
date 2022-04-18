def rskmndz():
    string = input() + ' запретил букву'
    for i in range(ord('а'), ord('я') + 1):
        if chr(i) in string:
            print(string.lstrip().rstrip(), chr(i))
            string = string.replace(chr(i), '')
            string = string.replace('  ', ' ')
