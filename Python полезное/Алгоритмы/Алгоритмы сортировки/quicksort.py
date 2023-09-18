from random import randint


massive = [randint(0, 100) for i in range(10)]


def quicksort(array):

    if len(array) <= 1:
        return array

    pivot = len(array) // 2

    less = [i for i in array if i < array[pivot]]
    equals = [i for i in array if i == array[pivot]]
    greater = [i for i in array if i > array[pivot]]

    return quicksort(less) + equals + quicksort(greater)


print(quicksort(massive))
