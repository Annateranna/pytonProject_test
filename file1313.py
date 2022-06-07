from decimal import *


def dec_sum():
    num = Decimal(input())
    t = num.as_tuple()
    if num < 1:
        print(max(t.digits))
    else:
        print(max(t.digits) + min(t.digits))