def sort_s(s):
    total = 0
    for i in range(len(s)):
        total += int(s[i])
    return total


s = input().split()
s = sorted(s, key=int)
s = sorted(s, key=sort_s)
print(*s)
