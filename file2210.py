def anton():
    n = int(input())
    list_all = [input() for _ in range(n)]
    for i in range(len(list_all)):
        if list_all[i].find('a') > -1:
            a_index = list_all[i].find('a')
            if list_all[i].find('n', a_index) > -1:
                n_index1 = list_all[i].find('n', a_index)
                if list_all[i].find('t', n_index1) > -1:
                    t_index = list_all[i].find('t', n_index1)
                    if list_all[i].find('o', t_index) > -1:
                        o_index = list_all[i].find('o', t_index)
                        if list_all[i].rfind('n', o_index) > -1:
                            print(i + 1, end=" ")
