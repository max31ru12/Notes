ln = int(input())
mas = list(map(int, input().split()))


min_index = 0
while min_index < ln - 1:
    left = 2 * min_index + 1
    if left <= ln - 1:
        min_index = left
    else:
        break

print(mas[min_index])