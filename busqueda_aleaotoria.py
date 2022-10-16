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
dimencions = [10,20,50,100]



# Definicion de las Funciones Objetivo
# ==============================================================================

# Funcion Unimodal Separable | Sphere
def unimodalSeparable(s): 
    y = 0
    for i in range(len(s)):
        y = round((s[i]*s[i]) + y, 2)
    
    return y


# Funcion unimodal Separable |  Griewank
def unimodalNoSeparable(s):
    # cv: varaible de control
    cv = 0         
    y =0
    for i in range(len(s)):
        cv = (s[i]+cv)
        y = cv*cv + y
    
    return y


# Funcion Multimodal separable( MS) | Rastrigin [-5.12, 5.12]
def multimodalSeparable(s):
    y = 0
    for i in range(0,len(s)):
        y = ((s[i])**2 -10*math.cos(2*math.pi*s[i]) + 10) + y
    
    return y


def multimodalNoSeparable(s):
    # Variables de control
    pt_g = 0
    st_g = 1
    for i in range(0,len(s)):
        pt_g = (1/4000)* s[i] + pt_g
        st_g = (math.cos(s[i])/math.sqrt(i+1))*st_g
    
    y = pt_g - st_g +1

    return y



# Vector solucion Inicial
# ==============================================================================
'''
    Funcion que genera el vector solucion inicial [s]  de tamaño nDim
'''
def vectorSolution(nDim):
    s= []
    for i in range(nDim):
        s.append(round(random.uniform(-100,100),2))      
    #print("Vector solucion inicial:", s)
    return s




# Implementacion del algoritmo (RANDOM -SEARCH)
# ==============================================================================

# Obtengo el la primera solucion de forma aleatoria - asigno a Best
for z in range(0,30):
    Best = vectorSolution(dimencions[3])
    print("Best: ", Best)
    # Evaluo la calidad de Best - de acuerdo a la funcion objetivo
    QBest = unimodalSeparable(Best)
    print("QBest: ",QBest)

    # Criterios de  parada
    NMEFO_Qs = 0
    NMEFO_QB = 0


    for i in range(0,5001):
        #Genero vector solucion s de forma aleatoria
        s = vectorSolution(dimencions[0])
        Qs = unimodalSeparable(s)
        #print("Vector s: ", s)
        #print("Calidad de s: ",Qs)
        #print("====================================================================")
        NMEFO_Qs = NMEFO_Qs+1
        if Qs < QBest:
            Best = s
            QBest = unimodalSeparable(Best)
            NMEFO_QB =NMEFO_QB+1
            #print("Entro: # veces NMEFO_Best: ",NMEFO_QB)
            
        magnitude = math.sqrt(sum(pow(element, 2) for element in Best))
        #print("Magnitud de Best : ",magnitude)

        # Integramos las condiciones de parada.
        if magnitude < 1 or (NMEFO_Qs + NMEFO_QB) >=5000:
            break

    print("Best Final iteracion: ",z," Calidad Best: ",QBest)


    # Guardamos los resultados en el excel para posteriores analisis
    # ==============================================================================
    dicc = {"Best": Best,
            "Qbest": QBest}

    df = pd.DataFrame([[dicc[key]] for key in dicc.keys()])
    df = df.transpose()


    with pd.ExcelWriter("../Resultados/resultados_algoritmos.xlsx",engine="openpyxl", mode = 'a', if_sheet_exists="overlay"
                        ) as writer:
        df.to_excel(writer, index=None, header = None, startrow=cont, sheet_name="10_dim_UNS")

    cont  = cont+1
    dicc = dict()