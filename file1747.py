n = int(input())
files = [input() for _ in range(n)]
for i in range(n):
    with open(files[i], 'r', encoding='utf-8') as input_file, open('output.txt', 'a', encoding='utf-8') as output_file:
        data = input_file.read()
        output_file.write(data)
