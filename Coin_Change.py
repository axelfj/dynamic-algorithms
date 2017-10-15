total = 11
coins = [1,5,10,21,25]

def coinChange(coinValueList,change):
    minCoins = [0] * (total + 1)
    coinsUsed = [0] * (total + 1)
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change], selectCoins(coinsUsed,total)

def selectCoins(coinsUsed,total):
    coin = total
    selection = []
    while coin > 0:
        thisCoin = coinsUsed[coin]
        selection += [thisCoin]
        coin -= thisCoin
    return selection

print(coinChange(coins,total))