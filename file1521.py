def count_args(*args):
    return len(args)


def sq_sum(*args):
    total = 0
    for i in args:
        total += i ** 2
    return total


def mean(*args):
    l = []
    for i in args:
        if type(i) == float or type(i) == int:
            l.append(i)
    if len(l) > 0:
        return sum(l) / len(l)
    else:
        return float(sum(l))


def greet(name, *args):
    answer = 'Hello, ' + name
    for i in args:
        answer += ' and ' + i
    answer += '!'
    return answer


def print_products(*args):
    i = 1
    for s in args:
        if type(s) == str and s != '':
            prods = str(i) + ') ' + s
            print(prods)
            i += 1
    if i == 1:
        print('Нет продуктов')


def info_kwargs(**kwargs):
    kwargs_sorted = sorted(kwargs)
    for k in kwargs_sorted:
        print(k, ': ', kwargs[k], sep='')


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')