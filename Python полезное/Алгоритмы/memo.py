def memo(coinValueList, change, knownResults):
    min_coins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif change in knownResults:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            num_coins = 1 + memo(coinValueList, change - i, knownResults)
            if num_coins < min_coins:
                min_coins = num_coins
                knownResults[change] = min_coins
    return min_coins


kn = {}
print(memo([1, 5, 10, 21, 25], 63, kn))
print(kn)
