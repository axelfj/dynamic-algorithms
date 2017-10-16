# This algorithm search the minimum ammount of coins to give change back #
# Input: Coins & Change.
#   Coins is a list with the values of the coins, the change is what you're aiming to reach with the minimum of coins #
# Output: Minimum value & Selection of coins.
#   The coinChange algorithm searches the minimum value and selectCoins makes the selections of the coins.

def coinChange(coins, change):
    minCoins = [0] * (total + 1)
    coinsUsed = [0] * (total + 1)
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coins if c <= cents]:
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