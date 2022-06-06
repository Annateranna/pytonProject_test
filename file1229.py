import random
import string


def generate_password(length):
    s1 = set(string.digits) - set('01')
    s2 = set(string.ascii_uppercase) - set('IO')
    s3 = set(string.ascii_lowercase) - set('lo')
    s = random.sample(s1, length // 3) + random.sample(s2, length // 3) + random.sample(s3, (length - (length // 3) - (length // 3)))
    passw = ''.join(s)
    return passw


def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))


def generate_all():
    n, m = int(input()), int(input())
    generate_passwords(n, m)