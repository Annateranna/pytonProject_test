with open('ledger.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
    total = sum(list(map(int, list(map(lambda x: x.rstrip('\n').lstrip('$'), data)))))
    print('$', total, sep='')
