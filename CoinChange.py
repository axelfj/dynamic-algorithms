# This algorithm search the minimum ammount of coins to give change back #
# Input: Coins & Change.
#   Coins is a number, the change is what you're aiming to reach with the minimum of coins #
# Output: Minimum value & Selection of coins.
#   The coinChange algorithm searches the minimum value and selectCoins makes the selections of the coins.

def coinChange(coins, change):

    def createCoins(coins):
        arrayCoins = [x for x in range(1,coins+1)]
        return arrayCoins

    def selectCoins(coinsUsed, total):
        coin = total
        selection = []
        while coin > 0:
            thisCoin = coinsUsed[coin]
            selection += [thisCoin]
            coin -= thisCoin
        return selection

    coins = createCoins(coins)
    minCoins = [0] * (change + 1)
    coinsUsed = [0] * (change + 1)
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coins if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin

    return "The quantity of coins is:\t",minCoins[change], "\nThe coins you should use:\t",selectCoins(coinsUsed,change)