def queen():
    ch = input()
    step = ch[1] + ch[0]
    matrix = []
    ind_i = 0
    ind_j = 0

    for i in range(8, 0, -1):
        temp = [(str(i) + chr(j)) for j in range(97, 105)]
        matrix.append(temp)

    for i in range(8):
        for j in range(8):
            if step == matrix[i][j]:
                ind_i = i
                ind_j = j

    for i in range(8):
        for j in range(8):
            if i == ind_i and j == ind_j:
                print('Q', end=' ')
            elif (abs(ind_i - i) == abs(ind_j - j)) or ((ind_j != j and ind_i == i) or (ind_j == j and ind_i != i)):
                print('*', end=' ')
            else:
                print('.', end=' ')
        print()
