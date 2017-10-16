from random import *

# This algorithm sorts an array of n elements. #
# Input: Array.
#   QuickSort use a pivot number and creates two sub-arrays and use the same method until the array is empty.
# Output: sorted array
#   QuickSort returns the sorted array.

def randomArray(x):
    array = []
    for i in range(x):
        array.append(randint(i,999999))
    return array
        
def quickSort(array):
    if array == []:
        return []
    else:
        pivot = array[0]
        leftValues = [x for x in array[1:] if x < pivot]
        rightValues = [x for x in array[1:] if x >= pivot]
        return quickSort(leftValues)+[pivot]+quickSort(rightValues)