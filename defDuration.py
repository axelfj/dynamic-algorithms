import datetime
import sys

from Backpack_Problem import *

sys.setrecursionlimit(10000)

def medirDuracion(funcion):
    tiempoInicial = datetime.datetime.now()
    funcion()
    tiempoFinal = datetime.datetime.now()
    print("Duración de", funcion.__name__, ":", tiempoFinal - tiempoInicial)

    
medirDuracion(backpack([1,2,3,4],11))