import random


def password():
    list_l = [i for i in range(65, 91)] + [i for i in range(97, 123)]
    length = int(input())
    passw = ''
    
    for i in range(length):
        passw += chr(list_l[random.randrange(len(list_l))])

    print(passw)

