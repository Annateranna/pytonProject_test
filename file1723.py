import random

file_name = open('lines.txt', encoding='utf-8')

file_content = file_name.readlines()
line = random.randrange(len(file_content))
print(file_content[line])

file_name.close()
