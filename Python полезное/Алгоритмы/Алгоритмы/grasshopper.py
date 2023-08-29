def hop(n):
    mas = [0, 1]
    for i in range(2, n + 1):
        mas.append(hop(n - 1) + hop(n - 2))
    return mas[n]


print(hop(4))
