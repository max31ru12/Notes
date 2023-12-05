ln = int(input())
mas = list(map(int, input().split()))


min_index = 0
while min_index < ln - 1:
    left = 2 * min_index + 1
    if left <= ln - 1:
        min_index = left
    else:
        break

max_index = 0
while max_index < ln - 1:
    right = 2 * max_index + 2
    if right <= ln - 1:
        max_index = right
    else:
        break

print(mas[min_index] * mas[max_index])
