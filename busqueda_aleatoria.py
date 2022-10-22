# Algoritmo de busqueda Aletoria (RANDOM -SEARCH)
"""
    - Algoritmo de optimización global más simple y de exploración extrema.
    -  En las funciones de caldiad siempre se busca minimizar (min)
"""
import numpy as np
import pandas as pd
import random
import math

# Variables Globales
# ==============================================================================
cont = 1
dicc = dict()
dimencions = 100   #    20,50,100
rango = 600
seleccion = 4
NMEFO = 5000

nombreHojaExcell = str(dimencions)+"_BusquedaAleatoria"
NombreDocumento = "funsion"+str(seleccion)+"_BusquedaAleatoria.xlsx"
# 1. Funcion Unimodal Separable | Sphere            [-100, 100]
# 2. Funcion unimodal No Separable | Schwefel      [-100, 100]
# 3. Funcion Multimodal separable( MS) | Rastrigin  [-5.12, 5.12]
# 4. Funcion Multimodal No Separable (MNS) | Griewank [-600, 600]

# Definicion de las Funciones Objetivo
# ==============================================================================

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
def vectorSolution(nDim, rango):
    s= []
    for i in range(nDim):
        s.append(random.uniform(-rango,rango))    
    #print("Vector solucion inicial:", s)
    return s


# Implementacion del algoritmo (RANDOM -SEARCH)
# ==============================================================================

# Obtengo el la primera solucion de forma aleatoria - asigno a Best
for z in range(0,30):
    Best = vectorSolution(dimencions, rango)
    contEvaluacion = 0
    # Evaluo la calidad de Best - de acuerdo a la funcion objetivo
    calidadParada = funciones_matematicas(seleccion, Best, contEvaluacion)
    QBest = calidadParada[0]
    contEvaluacion = calidadParada[1]
    while QBest > 1:
        #Genero vector solucion s de forma aleatoria
        s = vectorSolution(dimencions, rango)
        calidadParada = funciones_matematicas(seleccion, s, contEvaluacion)
        Qs = calidadParada[0]
        contEvaluacion = calidadParada[1]
        if contEvaluacion == NMEFO:
            break 
        if Qs < QBest:
            Best = s
            QBest = Qs

    print("Best Final iteracion: ",z," Calidad Best: ",QBest)
    # Guardamos los resultados en el excel para posteriores analisis
    # ==============================================================================
    dicc = {"Best": Best,
            "Qbest": QBest}

    df = pd.DataFrame([[dicc[key]] for key in dicc.keys()])
    df = df.transpose()


    with pd.ExcelWriter(NombreDocumento,engine="openpyxl", mode = 'a', if_sheet_exists="overlay"
                        ) as writer:
        df.to_excel(writer, index=None, header = None, startrow=cont, sheet_name=nombreHojaExcell)

    cont  = cont+1
    dicc = dict()
