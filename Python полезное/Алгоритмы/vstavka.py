from random import randint


massive = [randint(0, 100) for i in range(10)]
print(massive)


def sorting(mas):

    for i in range(1, len(massive)):
        while i > 0 and mas[i - 1] > mas[i]:
            mas[i], mas[i-1] = mas[i-1], mas[i]
            i -= 1

    return mas


print(sorting(massive))




