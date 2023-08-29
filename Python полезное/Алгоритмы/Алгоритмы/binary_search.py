def binary_search(L, item):
    if len(L) == 0:
        return False
    median = len(L) // 2
    if item == L[median]:
        return True
    elif item < L[median]:
        return binary_search(L[:median], item)
    else:
        return binary_search(L[median + 1:], item)


massive = [i for i in range(101)]
print(binary_search(massive, 100))


# Другой формат бинарного поиска со сложностью Log(n)
def bs(L, item, left=0, right=None):
    if right is None:
        right = len(L)
    if right - left == 0:
        return False
    if right - left == 1:
        return L[left] == item
    median = (right + left) // 2
    if item < L[median]:
        return bs(L, item, left, median)
    else:
        return bs(L, item, median, right)


print(bs([1, 2, 3], 3))


# Вариант с циклом
def bss(L, item):
    left, right = 0, len(L)
    while right - left > 1:
        median = (right + left) // 2
        if item < L[median]:
            right = median
        else:
            left = median
    return right > left and L[left] == item
