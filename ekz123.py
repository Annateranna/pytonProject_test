def ekz():
    d = {
        1: "AEILNORSTU",
        2: "DG",
        3: "BCMP",
        4: "FHVWY",
        5: "K",
        8: "JX",
        10: "QZ"
    }

    s = input()
    total = 0

    for c in s:
        for k, v in d.items():
            if c in v:
                total += k

    print(total)
    