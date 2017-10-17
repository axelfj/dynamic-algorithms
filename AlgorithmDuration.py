import datetime
import sys

sys.setrecursionlimit(10000)

from Quicksort import*
from HeapSort import*
from HanoiTowers import *

def sortDuration(function, array):
    beginTime = datetime.datetime.now()
    function(array)
    finalTime = datetime.datetime.now()
    return "Duración del algoritmo:\t", finalTime - beginTime

def hanoiDuration(function, height):
    beginTime = datetime.datetime.now()
    function(height)
    finalTime = datetime.datetime.now()
    print(beginTime,finalTime)
    return "Duración del algoritmo:\t", finalTime - beginTime