coins = [1,2,3,4]
total = 11

def minCoins(coins, total):
    cols = total + 1
    rows = len(coins)
    T = [[0 if col == 0 else float("inf") for col in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(1, cols):
            if j < coins[i]:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = min(T[i - 1][j], 1 + T[i][j - coins[i]])
    return T[rows - 1][cols - 1], selectCoins(T[rows-1],coins)

def selectCoins(R, coins):
    selection = []
    start = len(R) - 1
    print(R)
    if R[start] == -1:
        return "No Solution Possible."
    while start >= 0:
        coin = coins[R[start]]
        selection += [coin]
        start = start - coin
    return selection

print(minCoins(coins, total))