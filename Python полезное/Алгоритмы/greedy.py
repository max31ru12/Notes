def greedy(coin_list, change):
    coin_list.sort(reverse=True)
    coin_number = 0
    for coin in coin_list:
        coin_number += change // coin
        change %= coin
    return coin_number


print(greedy([1, 5, 25], 63))
