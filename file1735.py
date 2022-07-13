with open('nums.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    for c in data:
        if c.isalpha():
            data = data.replace(c, ' ')
    numbers = data.split()
    print(numbers)
    print(sum(map(int, numbers)))
