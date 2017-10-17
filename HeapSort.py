# This is the Heap algorithm.
# You need to build the tree with the array identation.
# When you're building it, you make swaps between the leafNodes and the parent.
# Depending on the case, you'll need to move a bigger value to the parent.
# Otherwise you'll move the smaller.
# The childrens are represented this way:
#       - The parent is <parentPos>
#       - The left children is always 2(<parentPos>+1)
#       - The right children is always 2(<parentPos>+2)

from random import randint

def randomArray(x):
    array = []
    for i in range(x):
        array.append(randint(i,999999))
    return array

# MaxHeap
def maxHeap(array, lenArray, i):
    parent = i
    leftChild = i*2+1
    rightChild = i*2+2
    if leftChild < lenArray and array[parent] < array[leftChild]:
        parent = leftChild
    if rightChild < lenArray and array[parent] < array[rightChild]:
        parent = rightChild
    if parent != i:
        array[i],array[parent] = array[parent],array[i]
        maxHeap(array, lenArray, parent)
def maxHeapSort(array):
    lenArray = len(array)
    for i in range(lenArray, -1, -1):
        maxHeap(array,lenArray,i)
    for i in range(lenArray-1, 0, -1):
        array[i],array[0] = array[0],array[i]
        maxHeap(array, i, 0)
    return array

# MinHeap
def minHeap(array, lenArray, i):
    parent = i
    leftChild = i*2+1
    rightChild = i*2+2
    if leftChild < lenArray and array[parent] > array[leftChild]:
        parent = leftChild
    if rightChild < lenArray and array[parent] > array[rightChild]:
        parent = rightChild
    if parent != i:
        array[i],array[parent] = array[parent],array[i]
        maxHeap(array,len(array), parent)
def minHeapSort(array):
    lenArray = len(array)
    for i in range(lenArray,-1,-1):
        minHeap(array,lenArray,i)
    for i in range(lenArray-1,0,-1):
        array[i],array[0] = array[0],array[i]
        minHeap(array,i,0)
    return array