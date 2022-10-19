from random import random
import random
from math import dist
import math
import pandas as pd
import numpy as np

# Definimos las variables iniciales
#==============================================================================
longitudPermanencia = 4 # longitud de la lista tabu  (50, 100, 150)
n = 4  # numero de vecinos  (10, 20)
r = 1 # paso del tweak  (0.2, 06, 1.0)
nDim = 4 # numero de dimensiones de la funsion  (20, 50, 100)
rango = [-100, 100]
NMEFO = 5000  # maximo numero de evaluaciones de la funcion objetivo
cont = 1    # Para guardar registros
dicc = dict()
seleccion = 1
iteracionActual = 0
# 1. Funcion Unimodal Separable | Sphere
# 2. Funcion unimodal No Separable |  Griewank
# 3. Funcion Multimodal separable( MS) | Rastrigin [-5.12, 5.12]
# 4. Funcion Multimodal No Separable (MNS) | Ackley [-32, 32]

# Definicion de las Funciones Objetivo
# ==============================================================================

# Funcion Unimodal Separable | Sphere

def funciones_matematicas (seleccion, s, contEvaluacion):

    if seleccion == 1:
        # unimodalSeparable(s,contEvaluacion):
        contEvaluacion += 1
        y = 0
        for i in range(len(s)):
            y = round((s[i]*s[i]) + y, 2)
        
        return (y, contEvaluacion)
    
    elif seleccion == 2:
        # Funcion unimodal No Separable |  Griewank
        # cv: varaible de control
        cv = 0         
        y =0
        contEvaluacion += 1
        for i in range(len(s)):
            cv = (s[i]+cv)
            y = cv*cv + y
        
        return (y, contEvaluacion)


        # Funcion Multimodal separable( MS) | Rastrigin [-5.12, 5.12]
    elif seleccion == 3:
        y = 0
        contEvaluacion += 1
        for i in range(0,len(s)):
            y = ((s[i])**2 -10*math.cos(2*math.pi*s[i]) + 10) + y
        
        return (y, contEvaluacion)

    elif seleccion == 4:
        # Variables de control
        pt_g = 0
        st_g = 1
        contEvaluacion += 1
        for i in range(0,len(s)):
            pt_g = (1/4000)* s[i] + pt_g
            st_g = (math.cos(s[i])/math.sqrt(i+1))*st_g
        
        y = pt_g - st_g +1

        return (y, contEvaluacion)


# Vector solucion Inicial
# ==============================================================================
'''
    Funcion que genera el vector solucion inicial [s]  de tamaño nDim
'''
def vectorSolution(nDim):
    s= []
    for i in range(nDim):
        s.append(round(random.uniform(-100,100)))      
    #print("Vector solucion inicial:", s)
    return s

# Funciones tweak
# ==============================================================================

# Generacion del tweak
def genracionTW (s):
    tw = []
    for i in range(len(s)):
        tw.append(random.uniform(-r,r))
    return tw

# Funcion de probabilidad para aplicar al tweak
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


# Funcion para aplicar tweak
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

# Funcion para agregar caracteristicas a la lista tabu
def creacion_tuplas(list1, list2, C):
    list1 = np.array(list1)
    list2 = np.array(list2)
    posiciones = np.where(list1 != list2)
    posiciones = posiciones[0]
    ListaPosiciones = list(posiciones)
    listFinal = [ListaPosiciones, C]
    return listFinal

# Evaluacion del algoritmo
#================================================================================

s = []
listaCaracteristicas = []
C = 0   # Contador de la iteracion actual
contEvaluacion = 0   # variable para almacenar la NMEFO
s = vectorSolution(nDim)
print("Vector S inicial", s)
best = s

calidadParada = funciones_matematicas(seleccion, s, contEvaluacion)
QS = calidadParada[0]

calidadParada = funciones_matematicas(seleccion, best, contEvaluacion)
QBest = calidadParada[0]

#print("Calidad de S: ", QS)
#print("Calidad de best: ", QBest)
if iteracionActual > 1:
    for i in range(len(listaCaracteristicas)):
        if iteracionActual - listaCaracteristicas[i][1] > longitudPermanencia:
else:
    iteracionActual += 1
    tw_R = genracionTW (s)
    print(f"Tw de R: {tw_R}")
    R=aplicar_tweck(s, tw_R)
    print("vector R", R)
    # Calculamos calidad de R
    
    calidadParada = funciones_matematicas(seleccion, R, contEvaluacion)
    QR = calidadParada[0]
    contEvaluacion = calidadParada[1]
    print("Calidad de R", QR)
    # Generamos los vecinos
    for i in range(0,n-1):
        tw_W = genracionTW(s)
        print(f"Tw de W: {tw_W}")
        # Aplicamos Twick a W
        W = aplicar_tweck(s, tw_W)
        print(f"Vector W: {W}")
        
        # Evaluammos W
        calidadParada = funciones_matematicas(seleccion, W, contEvaluacion)
        QW = calidadParada[0]
        contEvaluacion = calidadParada[1]
        if contEvaluacion == NMEFO:
            break   
        print(f"calidad de W: ", QW, contEvaluacion)
        if (QW<QR):
            R = W
            QR = QW
            print("================")
            print("Calidad de R ", QR)
    print("Vector S", s)
    print("Vector R", R)
    ListaTupla =  creacion_tuplas(s,R,iteracionActual)   
    listaCaracteristicas.append(ListaTupla)
    S = R
    QS = QR
    if QS < QBest:
        Best = s
        QBest = QS
    print("Calidad de best", QBest)
    print("Longitud de la lista", listaCaracteristicas)
            
