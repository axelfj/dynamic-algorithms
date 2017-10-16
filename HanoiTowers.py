# This algorithm search the way to move disk from one tower to another with just one rule.
# You can't put a big disk over a small one. #
# Input: height, initTower, middleTower, finalTower
# Output: initTower, middleTower, finalTower
#   we put this to prove we sent from the initTower to the finalTower every disk

def hanoi(height):
    initTower = [i if i > 0 else i for i in range(height,0,-1)]
    finalTower = []*height
    middleTower = []*height
    def hanoiAux(height, initTower, middleTower, finalTower):
        if height > 0:
            hanoiAux(height - 1, initTower, finalTower, middleTower)
            finalTower.append(initTower.pop())
            hanoiAux(height - 1, middleTower, initTower, finalTower)
        return initTower, middleTower, finalTower
    return hanoiAux(height,initTower,middleTower,finalTower)