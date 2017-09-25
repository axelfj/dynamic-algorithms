# A, B and C are our towers. We need to formulate the way that you move all the disk from A to C.
# The condition is, you can't put a bigger disk over a smaller.

A = []
B = []
C = []

# We receive the height and the three towers.
def hanoiTowers(height, A, B, C):
    for i in range(height):
        A.append(i+1)
        B.append(0)
        C.append(0)
    A = A[::-1]
    print(A,B,C)

moveTower(5,A,B,C)

