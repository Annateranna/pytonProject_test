with open('words.txt', 'r', encoding='utf-8') as file:
    words = file.read().split()
    max_words = list(filter(lambda x: x if len(x) == len(max(words, key=len)) else '', words))
    print(*max_words, sep='\n')
