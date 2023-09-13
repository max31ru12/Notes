import time


def decor(function):
    def wrapper(*args, **kwargs):

        start = time.time()
        res = function(*args)

        end = time.time() - start
        print(end)

        return res

    return wrapper


@decor
def vstavka(massive: list):

    for i in range(1, len(massive)):

        while i > 0:

            if massive[i] < massive[i - 1]:
                massive[i], massive[i - 1] = massive[i - 1], massive[i]

            i -= 1

    return massive


print(vstavka([4, 3, 2, 1]))
