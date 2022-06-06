import random


def pi_value():
    n = 10 ** 6
    k = 0
    s0 = 4
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x * x + y * y <= 1:
            k += 1

    print((k / n) * s0)

