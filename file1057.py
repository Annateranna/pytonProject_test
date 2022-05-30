def dict_ord():
    words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

    result = {k: [ord(i) for i in k] for k in words}

    print(result)