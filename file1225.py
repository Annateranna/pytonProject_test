import random


def anagramma():
    s = [c for c in input()]
    random.shuffle(s)
    print(''.join(s))
