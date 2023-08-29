from random import randint
import time

massive = [randint(0, 100) for i in range(10)]


def decorator_function(func):

    def wrapper(*args, **kwargs):

        start = time.time()
        func(*list(args))
        end = time.time() - start
        print(end)

    return wrapper


@decorator_function
def sorting(mas):

    for i in range(1, len(mas)):

        while i > 0:
            if mas[i] < mas[i - 1]:
                mas[i], mas[i - 1] = mas[i - 1], mas[i]
            i -= 1

    return print(mas)


sorting(massive)

