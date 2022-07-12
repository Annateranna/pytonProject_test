file_name = open('prices.txt', encoding='utf-8')

file_content = file_name.read().split('\n')

prices = [p.split('\t') for p in file_content]
numbers = []

for i in range(len(prices) - 1):
    numbers.append(int(prices[i][1]) * int(prices[i][2]))

print(sum(numbers))


file_name.close()
