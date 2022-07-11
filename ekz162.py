def pretty_print(data, side='-', delimiter='|'):
    side_str = ''
    string = ''
    for i in range(len(data)):
        side_str += side + side * len(str(data[i])) + side * 2
        string += f'{delimiter} {data[i]} '
    string += f'{delimiter}'
    print('', side_str[1:])
    print(string)
    print('', side_str[1:])


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')
