def tails():
    list_tails = input()
    count = 0
    list_counts = [count]
    for c in list_tails:
        if c == "Р":
            count += 1
        else:
            count = 0
        list_counts.append(count)
    list_counts = sorted(list_counts, reverse=True)
    print(list_counts[0])
