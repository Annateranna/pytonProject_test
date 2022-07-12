file_name = open('numbers.txt', encoding='utf-8')

file_content = file_name.readlines()
num1 = int(file_content[0])
num2 = int(file_content[1])

print(num1 + num2)

file_name.close()