def dict_n_s():
    s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
    s = s.split()
    k, v = [], []

    for i in range(len(s)):
        temp = s[i].split(":")
        k += [int(temp[0])]
        v += [temp[1]]

    result = dict(zip(k, v))
    print(result)
