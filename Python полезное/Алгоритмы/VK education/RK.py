def can(count, size, H, W):
    rows = size // H
    columns = size // W
    return rows * columns >= count


def search(count, H, W):
    l = 0
    r = count * H
    while l + 1 < r:
        m = l + (r - 1) // 2
        if can(count, m, H, W):
            r = m
        else:
            l = m
    return r


print(search(13, 5, 3))
