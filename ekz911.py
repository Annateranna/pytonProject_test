def test():
    n, m, k, p = int(input()), int(input()), int(input()), int(input())
    total = n - (m - p) - p - (k - p)
    print(total)
