def tuples_sum():
    numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
    list_l = [0] * len(numbers)
    for i in range(len(numbers)):
        list_l[i] = sum(numbers[i]) / len(numbers[i])

    print(list_l)
