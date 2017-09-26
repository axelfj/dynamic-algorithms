from random import *


# The childrens are represented this way:
#       - The left children is always 2(<fatherPos>+1)
#       - The right children is always 2(<fatherPos>+2)

def randomArray(x):
    array = []
    for i in range(x):
        array.append(randint(i,999999))
    return array

def minHeapSort(array):
    return sorted(array)

def maxHeapSort(array):

    return sorted(array)

print(minHeapSort(randomArray(9)))