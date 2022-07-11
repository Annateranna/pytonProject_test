def add3(x):
    return x + 3


def mul7(x):
    return x * 7


def compose(f, g):
    def temp(x):
        return(f(g(x)))
    return temp


print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))
