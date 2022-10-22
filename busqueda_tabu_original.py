from random import random
import random
from math import dist
import math
import pandas as pd
import numpy as np

# Definimos las variables iniciales
#==============================================================================
nDim = 20 # numero de dimensiones de la funsion  (20, 50, 100)
excel = "resultados_tabu_20dim_funsion4.xlsx" # Nombre del archivo excell donde se guardaran los resultados
ListaR = [0.2, 0.6, 1.0] # paso del tweak  (0.2, 06, 1.0)
ListaN = [10, 20]  # numero de vecinos  (10, 20)
ListaTabu = [50, 100, 150] # longitud de la lista tabu  (50, 100, 150)

NMEFO = 5000  # maximo numero de evaluaciones de la funcion objetivo
seleccion = 4
rango = 600
# 1. Funcion Unimodal Separable | Sphere            [-100, 100]
# 2. Funcion unimodal No Separable | Schwefel      [-100, 100]
# 3. Funcion Multimodal separable( MS) | Rastrigin  [-5.12, 5.12]
# 4. Funcion Multimodal No Separable (MNS) | Griewank [-600, 600]

# Definicion de las Funciones Objetivo
# ==============================================================================

# Funcion Unimodal Separable | Sphere

def funciones_matematicas (seleccion, s, contEvaluacion):

    if seleccion == 1:
        contEvaluacion += 1
        y = 0
        for i in range(len(s)):
            y = round((s[i]*s[i]) + y, 2)
        return (y, contEvaluacion)
    
    elif seleccion == 2:
        cv = 0         
        y =0
        contEvaluacion += 1
        for i in range(len(s)):
            cv = (s[i]+cv)
            y = cv*cv + y
        return (y, contEvaluacion)

    elif seleccion == 3:
        y = 0
        contEvaluacion += 1
        for i in range(0,len(s)):
            y = ((s[i])**2 -10*math.cos(2*math.pi*s[i]) + 10) + y
        return (y, contEvaluacion)

    elif seleccion == 4:
        pt_g = 0
        st_g = 1
        contEvaluacion += 1
        for i in range(0,len(s)):
            pt_g = (1/4000)* s[i]**2 + pt_g
            st_g = (math.cos(s[i])/math.sqrt(i+1))*st_g
        y = pt_g - st_g +1
        return (y, contEvaluacion)


# Vector solucion Inicial
# ==============================================================================
'''
    Funcion que genera el vector solucion inicial [s]  de tamaño nDim
'''
def vectorSolution(nDim,rango):
    s= []
    for i in range(nDim):
        s.append(random.uniform(-rango,rango))    
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
    return (Generaltwick)


# Evaluacion del algoritmo
#====================================================================================


for tw in range (len(ListaR)):
    for vecinos in range (len(ListaN)):
        for long in range(len(ListaTabu)):
            nomenclaturaHoja = str(nDim) + "_dim_"+ str(ListaR[tw]) + "tw_" + str(ListaN[vecinos])+"ve_"+str(ListaTabu[long])+"longlist"
            #print(nomenclaturaHoja)
            cont = 1
            dicc = dict()
            r = ListaR[tw]
            n = ListaN[vecinos]
            longitudListaTabu = ListaTabu[long]

            for z in range(0,30):
                s = []                      # Vector solucion inicial
                L = []                      # Lista de los vectores solucion
                contEvaluacion = 0          # Variable para almacenar la NMEFO
                s = vectorSolution(nDim, rango)    # Creamos el vector solucion inicial
                L.append(s)                 # agregamos la solucion inicial S a la lista tabu
                best = s
                calidadParada = funciones_matematicas(seleccion, s, contEvaluacion)
                QS = calidadParada[0]
                contEvaluacion = calidadParada[1] 
                QBest = QS
                
                while QBest > 0.2:
                    
                    # Calculamos el tweak de R
                    tw_R = genracionTW (s)
                    # Aplicamos el tweak a R
                    R=aplicar_tweck(s, tw_R)
                    # Calculamos calidad de R
                    calidadParada = funciones_matematicas(seleccion, R, contEvaluacion)
                    QR = calidadParada[0]
                    contEvaluacion = calidadParada[1]
                    if contEvaluacion == NMEFO:
                        break
                    
                    # Generamos los vecinos
                    #========================================================================
                    for i in range(0,n-1):
                        # Generamos el tweak a W
                        tw_W = genracionTW(s)
                        # Aplicamos Twick a W
                        W = aplicar_tweck(s, tw_W)
                        # Evaluammos W
                        calidadParada = funciones_matematicas(seleccion, W, contEvaluacion)
                        QW = calidadParada[0]
                        contEvaluacion = calidadParada[1]
                        if contEvaluacion == NMEFO:
                            break   

                        # Calculo las distancias euclidianas de R y W con cada elemento de L
                        ListaDistanciasEuclidianasW = funcion_distancia_euclidiana(L, W)
                        ListaDistanciasEuclidianasR = funcion_distancia_euclidiana(L, R)
                        # Funcion para comprobar distancias euclidianas
                        distanciaEuclidianaW = comprobar_distancia_euclidiana(ListaDistanciasEuclidianasW, 0.2)
                        distanciaEuclidianaR = comprobar_distancia_euclidiana(ListaDistanciasEuclidianasR, 0.2)

                        if (distanciaEuclidianaW==len(L)) and (QW<QR) or (distanciaEuclidianaR != len(L)):
                            R = W
                            QR = QW
                    if contEvaluacion == NMEFO:
                        break    
                    # Evaluo distancia euclidiana del nuevo R con todos los elementos de L
                    ListaDistanciasEuclidianasR = funcion_distancia_euclidiana(L, R)
                    # Funcion para comprobar la distancia euclidiana
                    distanciaEuclidianaR = comprobar_distancia_euclidiana(ListaDistanciasEuclidianasR, 0.1)
                    if (distanciaEuclidianaR==len(L)) and QR < QS:
                        s = R
                        QS = QR
                        L.append(R)
                    # Elimino el elemento mas viejo
                    if len(L) > longitudListaTabu:
                        L.pop(0)
                    if QS < QBest:    
                        best = s
                        QBest = QS
                print("Best Final iteracion: ",z," Calidad Best: ",QBest)
                # Guardamos los resultados en el excel para posteriores analisis
                # ==============================================================================
                dicc = {"Best": best,
                        "Qbest": QBest}

                df = pd.DataFrame([[dicc[key]] for key in dicc.keys()])
                df = df.transpose()


                with pd.ExcelWriter(excel,engine="openpyxl", mode = 'a', if_sheet_exists="overlay"
                                    ) as writer:
                    df.to_excel(writer, index=None, header = None, startrow=cont, sheet_name=nomenclaturaHoja)

                cont  = cont+1
                dicc = dict()
    
