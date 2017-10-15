def raiseTower(height):
    initTower = [i if i > 0 else i for i in range(height,0,-1)]
    finalTower = []*height
    middleTower = []*height
    return initTower,finalTower,middleTower

def hanoi(height, initTower, middleTower, finalTower):
    if height > 0:
        hanoi(height - 1, initTower, finalTower, middleTower)
        finalTower.append(initTower.pop())
        hanoi(height - 1, middleTower, initTower, finalTower)
    return initTower, middleTower, finalTower


initTower = [5, 4, 3, 2, 1]
finalTower = []
middleTower = []

#print(source, helper, target)
print(hanoi(len(initTower), initTower, middleTower, finalTower))
#print(raiseTower(5))