import random


def lottery():
    list_l = [i for i in range(1, 50)]
    lot = set()

    while len(lot) < 7:
        lot.update({list_l[random.randrange(len(list_l))]})

    print(*sorted(lot))
