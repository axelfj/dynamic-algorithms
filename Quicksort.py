from random import *

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

array = randomArray(10)
print(quickSort(array))
