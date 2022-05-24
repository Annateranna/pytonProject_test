def library():
    m, n = int(input()), int(input())
    set_l = {input() for _ in range(m)}

    for _ in range(n):
        print('YES' if input() in set_l else 'NO')
