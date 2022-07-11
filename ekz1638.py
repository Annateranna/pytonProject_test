def arithmetic_operation(func):
    result = {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, '/': lambda x, y: x/y}
    return result[func]


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))
