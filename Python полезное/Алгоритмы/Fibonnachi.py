# С рекусией

def fib(k):
    if k in [0, 1]:
        return k
    return fib(k - 1) + fib(k - 2)


print(fib(4))


# Без рекурсии
def feb(k):
    a, b = 0, 1
    for i in range(k):
        a, b = b, a + b
    return a


print(feb(4))
