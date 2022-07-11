n = int(input())
result = []
for i in range(n):
    k = int(input())
    classes = [input().split()[1] for _ in range(k)]
    result.append(any(list(map(lambda x: x == '5', classes))))

print('YES' if all(result) else 'NO')


