def key_sort(i):
    def comparador(num):
        return num[i - 1]
    return comparador


athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

i = int(input())
athlets = sorted(athletes, key=key_sort(i))

for j in athlets:
    print(*j)
