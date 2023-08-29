def sort(massive):
    if len(massive) == 1:
        return massive
    median = len(massive) // 2
    left_half = massive[:median]
    right_half = massive[median:]
    left = sort(left_half)
    right = sort(right_half)
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(right) or j < len(left):
        if j == len(left) or i < len(right) and right[i] < left[j]:
            result.append(right[i])
            i += 1
        else:
            result.append(left[j])
            j += 1
    return result


from random import randint
print(sort([randint(0, 100) for i in range(20)]))