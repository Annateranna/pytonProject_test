def dict_divider():
    numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
    value = [[]] * len(numbers)

    for i in range(len(numbers)):
        value[i] = [j for j in range(1, numbers[i] + 1) if numbers[i] % j == 0]

    result = dict(zip(numbers, value))

    print(result)

