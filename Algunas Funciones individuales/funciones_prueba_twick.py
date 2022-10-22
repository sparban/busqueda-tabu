
import numpy as np
import random

def vectorSolution(nDim):
    s= []
    for i in range(nDim):
        s.append(round(random.uniform(-100,100)))      
    #print("Vector solucion inicial:", s)
    return s

def genracionTW (s):
    tw = []
    for i in range(len(s)):
        tw.append(random.uniform(-1,1))
    return tw


# Funcion de probabilidad para aplicar al tweak
def funcion_probabilidad (s):
    probabilidad = []
    for i in range(len(s)):
        probabilidad.append(random.uniform(0,1))
    return probabilidad


def aplicar_tweck (s,tw):
    Generaltwick = []
    listaProbabillidad = funcion_probabilidad(s)
    for i in range(len(s)):
        if listaProbabillidad[i] > 0.5:
            Generaltwick.append(s[i]+tw[i])
        else:
            Generaltwick.append(s[i])
    #print("Lista de probabilidades", listaProbabillidad)
    return (Generaltwick)
s = []
W = []
s = vectorSolution(5)
tw = genracionTW(s)
W = aplicar_tweck (s, tw)

print("Vector S", s)
print("Vector W", W)

def creacion_tuplas(list1, list2, C):
    lst1 = np.array(list1)
    lst2 = np.array(list2)
    posiciones = np.where(list1 != list2)
    posiciones = posiciones[0]
    ListaPosiciones = list(posiciones)
    listFinal = [ListaPosiciones, C]
    return listFinal

