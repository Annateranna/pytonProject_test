def imt_1():
    kg, m = float(input()), float(input())
    imt = kg / m**2
    print(imt)
    if 18.5 <= imt <= 25:
        print('Оптимальная масса')
    elif imt > 25:
        print('Избыточная масса')
    else:
        print('Недостаточная масса')

