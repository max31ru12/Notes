count = 13
height = 5
width = 3


def can(count, size, width, height):

    rows = size // height
    columns = size // width

    return rows * columns >= count


def search(count, H, W):
    l = 0
    r = count * height
    while l + 1 < r:
        m = l + (r - 1) // 2
        if can(count, m, W, H):
            r = m
        else:
            l = m
    return r


print(search(13, 5, 3))
