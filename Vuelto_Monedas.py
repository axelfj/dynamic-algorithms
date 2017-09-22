from random import *

x = int(randrange(0,99999))

coins = [1,2,3]
total = 5
matrix = []

def change(coins, total):
    for i in range(len(coins)):
        row = [x*0 for x in range(total+1)]
        matrix.append(row)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j >= coins[i]:
                matrix[i][j] = coins[i] + matrix[i-1][j-coins[i]]
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[len(coins)-1][total]

print(change(coins,total))