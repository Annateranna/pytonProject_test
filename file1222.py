import random
import string


def generate_index():
    numbers = [i for i in range(100)]
    ip_index = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + \
               str(random.choice(numbers)) + '_' + str(random.choice(numbers)) + random.choice(string.ascii_uppercase) + \
               random.choice(string.ascii_uppercase)

    return ip_index
