import datetime
import sys

sys.setrecursionlimit(10000)

def medirDuracion(funcion):
    tiempoInicial = datetime.datetime.now()
    funcion()
    tiempoFinal = datetime.datetime.now()
    print("Duración de", funcion.__name__, ":", tiempoFinal - tiempoInicial)