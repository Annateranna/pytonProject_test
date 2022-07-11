def concat(*args, sep=' '):
    string = ''
    for i in range(len(args) - 1):
        string += f'{str(args[i])}{sep}'
    string += str(args[len(args) - 1])
    return string


print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))