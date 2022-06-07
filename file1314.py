from decimal import *


def dec_exp():
    d = Decimal(input())
    print(Decimal.exp(d) + Decimal.log10(d) + Decimal.ln(d) + Decimal.sqrt(d))
