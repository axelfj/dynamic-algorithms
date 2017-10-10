from random import *

x = int(randrange(0,15))
coins = [1,2,3]
total = 5
vector = []

def change(coins, total):
    for i in coins:
        if i < 0:
            return "Can't get the change"
    for i in range(total + 1):
        vector.append(0)
        vector[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], total + 1):
            vector[j] += vector[j - coins[i]]
    return vector[total]


def selectCoins(coins,total):
    return

#print(change(coins, total))
