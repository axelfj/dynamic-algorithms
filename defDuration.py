import datetime
import sys

sys.setrecursionlimit(10000)

def sortDuration(function, array):
    beginTime = datetime.datetime.now()
    function(array)
    finalTime = datetime.datetime.now()
    print("Duración de", funcion.__name__, ":", finalTime - beginTime)

def hanoiDuration(function, height):
    beginTime = datetime.datetime.now()
    function(height)
    finalTime = datetime.datetime.now()
    print("Duración de", funcion.__name__, ":", finalTime - beginTime)

