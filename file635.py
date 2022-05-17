def parabola():
    a, b, c = int(input()), int(input()), int(input())
    parabola_tuple = (- b / (2 * a), (4 * a * c - b**2) / (4 * a))
    print(parabola_tuple)
