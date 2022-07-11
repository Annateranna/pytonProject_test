def decimal_view(ip):
    numbers = list(map(int, ip.split('.')))
    result = numbers[0] * 256**3 + numbers[1] * 256**2 + numbers[2] * 256 + numbers[3]
    return result


n = int(input())
ip_list = [input() for _ in range(n)]
print(*sorted(ip_list, key=decimal_view), sep='\n')
