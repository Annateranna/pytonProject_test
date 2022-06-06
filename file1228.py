import random
import string


def generate_password(length):
    s = string.digits + string.ascii_letters
    for c in s:
        if c == 'l' or c == 'I' or c == 'O' or c == 'o' or c == '0' or c == '1':
            s = s.replace(c, '')
    passw = ''.join(random.sample(s, length))
    return passw


def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))


def generate_all():
    n, m = int(input()), int(input())
    generate_passwords(n, m)
