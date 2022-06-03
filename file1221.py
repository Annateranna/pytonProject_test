import random


def generate_ip():
    numbers = [i for i in range(256)]
    ip_addr = str(random.choice(numbers)) + '.' + str(random.choice(numbers)) + '.' + str(random.choice(numbers)) + '.'\
              + str(random.choice(numbers))

    return ip_addr
