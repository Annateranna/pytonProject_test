def online():
    m, n = int(input()), int(input())
    m_set = {input() for _ in range(m)}
    i_set = {input() for _ in range(n)}

    print(len(m_set - i_set))
