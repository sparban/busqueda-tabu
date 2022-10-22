# Busqueda tabu

from random import random
import random
from math import dist
#import numpy as np

l = 50 # nlongi
n = 3
r = 0.2 # paso del tweak
rango = [-100, 100]
s = []
contEvaluacion = 0   # variable para almacenar la NMEFO
NMEFO = 100  # maximo numero de evaluaciones de la funcion objetivo
numDimensiones = 5
# Creacion de las funciones objetivos (solucion inicial propuesta)
for i in range(numDimensiones):
    s.append(round(random.uniform(-100,100),2))      
print("Vector solucion inicial:", s)

# lista tabu
# agregamos el s a la lista tabu

L = []
L.append(s)   # agregamos la solucion inicial S a la lista tabu

# Evaluamos la funcion objetivo

# Funcion de calidad (Unimodal Separable)

def unimodalNoSeparable (s, contEvaluacion): 
    y = 0
    contEvaluacion += 1
    for i in range(len(s)):
        y = round((s[i]*s[i]) + y, 2)
    return (y, contEvaluacion)

# Funcion de evaluacion (unimodal no separable)

def unimodalSeparable(s, contEvaluacion):
    acum = 0
    y =0
    contEvaluacion += 1
    for i in range(len(s)):
        acum = (s[i]+acum)
        y = acum*acum + y
    return(y, contEvaluacion)

# Generamos el tweak

def genracionTW (s):
    tw = []
    for i in range(len(s)):
        tw.append(random.uniform(-r,r))
    return tw

# Funcion generacion de probabilidades
def funcion_probabilidad (s):
    probabilidad = []
    for i in range(len(s)):
        probabilidad.append(random.uniform(0,1))
    return probabilidad

# Funcion calculo distancias euclidianas
def funcion_distancia_euclidiana (L, listaEvaluacion):
    ListaDistanciasEuclidianas = []
    for i in range (len(L)):
        ListaDistanciasEuclidianas.append(dist(L[i],listaEvaluacion))
    return ListaDistanciasEuclidianas

# Funcion comprobar distancias euclidianas
def comprobar_distancia_euclidiana(listaEvaluacion, distanciaEvaluar):
    count = 0
    for i in range(len(listaEvaluacion)):
        if listaEvaluacion[i] > distanciaEvaluar:
            count += 1
    return count

def aplicar_tweck (s,tw_R):
    listaProbabillidad = funcion_probabilidad(s)
    for i in range(len(s)):
        if listaProbabillidad[i] > 0.5:
            R.append(s[i]+tw_R[i])
        else:
            R.append(s[i])
    return R

best = s
print(contEvaluacion)
#QBest = 10
# Condicion de evaluacion del minimo encontrado
while contEvaluacion < 20:

    calidadParada = unimodalNoSeparable(s, contEvaluacion)
    QS = calidadParada[0]
    contEvaluacion = calidadParada[1]
    if contEvaluacion == NMEFO:
        break
    print("Calidad de S: ", QS, contEvaluacion)
    
    calidadParada = unimodalNoSeparable(best, contEvaluacion)
    QBest = calidadParada[0]
    contEvaluacion = calidadParada[1]
    if contEvaluacion == NMEFO:
        break
    print("Calidad de best: ", QBest, contEvaluacion)

    print("Lista tabu: ", L)
    
    # Aplicamos el tweak al vector solucion
    R = []
    tw_R = genracionTW (s)
    print(f"Tw de R: {tw_R}")
    # llamamos funcion de probabilidades y aplicamos el twick a R
    R = aplicar_tweck(s,tw_R)
    print(f"Vector R: {R}")
    # llamamos a la funcion para evaluacion
    calidadParada = unimodalNoSeparable(R, contEvaluacion)
    QR = calidadParada[0]
    contEvaluacion = calidadParada[1]
    if contEvaluacion == NMEFO:
        break
    print(f"calidad de R:", QR, contEvaluacion)


    # Generamos los vecinos
    for i in range(0,n-1):
        W = []
        print("----------------------------------------------------------")
        tw_W = genracionTW(s)
        print(f"Tw de W: {tw_W}")
        # Aplicamos Twick a W
        W = aplicar_tweck(s,tw_W)
        print(f"Vector W: {W}")   
        # Evaluammos W
        
        calidadParada = unimodalNoSeparable(W, contEvaluacion)
        QW = calidadParada[0]
        contEvaluacion = calidadParada[1]
        if contEvaluacion == NMEFO:
            break   
        print(f"calidad de W: ", QW, contEvaluacion)
        # Evaluo distancia euclidiana con la lista tabu
        
        ListaDistanciasEuclidianasW = funcion_distancia_euclidiana(L, W)
        ListaDistanciasEuclidianasR = funcion_distancia_euclidiana(L, R)
        distanciaEuclidianaW = comprobar_distancia_euclidiana(ListaDistanciasEuclidianasW, 0.3)
        distanciaEuclidianaR = comprobar_distancia_euclidiana(ListaDistanciasEuclidianasR, 0.3)
        if (distanciaEuclidianaW==len(L)) and (QW>QR) or (distanciaEuclidianaR != len(L)):
            R = W
            QR = QW
            print("Se cumple")
            print(f"Distancia euclidiana W {distanciaEuclidianaW}")
            print(f"Distancia euclidiana R {distanciaEuclidianaR}")
                
        
    if contEvaluacion == NMEFO:
        break    
    print ("Valor final de R despues de los vecinos", R)   
    
    
    if not(R in L) and QR > QS:
        print("Se cumple 2")
        s = R
        L.append(R)
        
        if len(L) > l:
            L.pop(0)
        print("Lista final despues de todo el procedimiento:",L)

    if QS > QBest:    
        best = s
        print(f"Valor final de R: {R}")
    print(f"taamaño de la lista: {len(L)}")
print("Mejor calidada", QBest)
        