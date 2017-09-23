from random import *

x = int(randrange(0,15))
coins = [1,2,3]
total = x
matrix = []

def change(coins, total):
    for i in range(total + 1):
        matrix.append(0)
    matrix[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], total + 1):
            matrix[j] += matrix[j - coins[i]]
    return matrix

print(change(coins, total))
