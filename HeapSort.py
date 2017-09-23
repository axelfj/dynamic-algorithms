from random import *

def randomArray(x):
    array = []
    for i in range(x):
        array.append(randint(i,x))
    return array

def heapSort(array):
    return sort(array)