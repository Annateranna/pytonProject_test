def str_cost():
    s = input()
    length_in_k = len(s) * 60
    ruble = length_in_k // 100
    kopeika = length_in_k - ruble * 100
    print(ruble, 'р.', kopeika, 'коп.')