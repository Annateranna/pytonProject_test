import random
import string


def lottery_tickets():
    for _ in range(100):
        first = str(random.randint(1, 9))
        others = ''.join(random.sample(string.digits, 6))
        print(first + others)

