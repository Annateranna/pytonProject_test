file_name = open(input(), encoding='utf-8')
file_content = file_name.readlines()
print(file_content[len(file_content) - 2])
file_name.close()
