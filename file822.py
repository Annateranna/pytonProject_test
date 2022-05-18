def books():
    n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), \
                             int(input()), int(input())

    one_book = t + x + z - m - n - k + t + y + x - m - n - k + t + y + z - m - n - k
    two_books = n - z - t + k + m - y - t + k + n - x - t + m
    nothing = a - one_book - two_books - t
    print(one_book, two_books, nothing, sep='\n')
