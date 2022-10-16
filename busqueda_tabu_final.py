from random import random
import random
from math import dist
import math
import pandas as pd
import numpy as np
# Definimos las variables iniciales
#===================================================
longitudListaTabu = 50 # longitud de la lista tabu
n = 10  # numero de vecinos
r = 0.2 # paso del tweak
nDim = 20
rango = [-100, 100]
NMEFO = 50000  # maximo numero de evaluaciones de la funcion objetivo
cont = 1
dicc = dict()

# Definicion de las Funciones Objetivo
# ==============================================================================

# Funcion Unimodal Separable | Sphere
def unimodalSeparable(s,contEvaluacion): 
    contEvaluacion += 1
    y = 0
    for i in range(len(s)):
        y = round((s[i]*s[i]) + y, 2)
    
    return (y, contEvaluacion)


# Funcion unimodal No Separable |  Griewank
def unimodalNoSeparable(s, contEvaluacion):
    # cv: varaible de control
    cv = 0         
    y =0
    contEvaluacion += 1
    for i in range(len(s)):
        cv = (s[i]+cv)
        y = cv*cv + y
    
    return (y, contEvaluacion)


# Funcion Multimodal separable( MS) | Rastrigin [-5.12, 5.12]
def multimodalSeparable(s, contEvaluacion):
    y = 0
    contEvaluacion += 1
    for i in range(0,len(s)):
        y = ((s[i])**2 -10*math.cos(2*math.pi*s[i]) + 10) + y
    
    return (y, contEvaluacion)


def multimodalNoSeparable(s, contEvaluacion):
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
        s.append(round(random.uniform(-100,100),2))      
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
    return Generaltwick





# Evaluacion del algoritmo
#================================================================================

for z in range(0,30):
    s = []
    L = []
    contEvaluacion = 0   # variable para almacenar la NMEFO
    s = vectorSolution(nDim)
    L.append(s)   # agregamos la solucion inicial S a la lista tabu
    best = s
    QBest = 1000
    while QBest > 1:
        
        calidadParada = unimodalSeparable(s, contEvaluacion)
        QS = calidadParada[0]
        contEvaluacion = calidadParada[1]
        if contEvaluacion == NMEFO:
            break
        #print("Calidad de S: ", QS, contEvaluacion)
        
        
        calidadParada = unimodalSeparable(best, contEvaluacion)
        QBest = calidadParada[0]
        contEvaluacion = calidadParada[1]
        if contEvaluacion == NMEFO:
            break
        #print("Calidad de best: ", QBest, contEvaluacion)
        
        
        # llamamos funcion de probabilidades y aplicamos el twick a R
        tw_R = genracionTW (s)
        #print(f"Tw de R: {tw_R}")
        R=aplicar_tweck(s, tw_R)
        
        # Calculamos calidad de R
        
        calidadParada = unimodalSeparable(R, contEvaluacion)
        QR = calidadParada[0]
        contEvaluacion = calidadParada[1]
        if contEvaluacion == NMEFO:
            break
        #print(f"calidad de R:", QR, contEvaluacion)
        
        
        # Generamos los vecinos
        for i in range(0,n-1):
            tw_W = genracionTW(s)
            #print(f"Tw de W: {tw_W}")
            # Aplicamos Twick a W
            W = aplicar_tweck(s, tw_W)
            #print(f"Vector W: {W}")
            
            # Evaluammos W
            calidadParada = unimodalSeparable(W, contEvaluacion)
            QW = calidadParada[0]
            contEvaluacion = calidadParada[1]
            if contEvaluacion == NMEFO:
                break   
            #print(f"calidad de W: ", QW, contEvaluacion)
            
            
            
            # Evaluo distancia euclidiana con la lista tabu
            
            '''print("********************************************************")
            print("lista L", L)
            print("vector W", W)
            print("vector R", R)
            print("longitud L", len(L))
            '''
            ListaDistanciasEuclidianasW = funcion_distancia_euclidiana(L, W)
            ListaDistanciasEuclidianasR = funcion_distancia_euclidiana(L, R)
            #print("ListaDistanciasEuclidianasW", ListaDistanciasEuclidianasW)
            #print("ListaDistanciasEuclidianasR", ListaDistanciasEuclidianasR)
            
            distanciaEuclidianaW = comprobar_distancia_euclidiana(ListaDistanciasEuclidianasW, 0.1)
            distanciaEuclidianaR = comprobar_distancia_euclidiana(ListaDistanciasEuclidianasR, 0.1)
            #print("pertenece W:", distanciaEuclidianaW)
            #print("pertenece R", distanciaEuclidianaR)
            if (distanciaEuclidianaW==len(L)) and (QW<QR) or (distanciaEuclidianaR != len(L)):
                R = W
                QR = QW
                #print("Se cumple")
                #print(f"Distancia euclidiana W {distanciaEuclidianaW}")
                #print(f"Distancia euclidiana R {distanciaEuclidianaR}")
            
        if contEvaluacion == NMEFO:
            break    
        #print ("Valor final de R despues de los vecinos", R)  
                    
        # Evaluacion distancia euclidiana 2

        ListaDistanciasEuclidianasR = funcion_distancia_euclidiana(L, R)
        #print("distancia euclidiana R final", ListaDistanciasEuclidianasR)
        distanciaEuclidianaR = comprobar_distancia_euclidiana(ListaDistanciasEuclidianasR, 0.1)
        #print("Valor final de los vecinos R", distanciaEuclidianaR)
        if (distanciaEuclidianaR==len(L)) and QR < QS:
            #print("Se cumple 2")
            s = R
            QS = QR
            L.append(R)
            
            # Elimino el elemento mas viejo
            if len(L) > longitudListaTabu:
                L.pop(0)
            #print("Lista final despues de todo el procedimiento:",L)

        if QS < QBest:    
            best = s

    print("Best Final iteracion: ",z," Calidad Best: ",QBest)
    
    # Guardamos los resultados en el excel para posteriores analisis
    # ==============================================================================
    dicc = {"Best": best,
            "Qbest": QBest}

    df = pd.DataFrame([[dicc[key]] for key in dicc.keys()])
    df = df.transpose()


    with pd.ExcelWriter("resultados_tabu.xlsx",engine="openpyxl", mode = 'a', if_sheet_exists="overlay"
                        ) as writer:
        df.to_excel(writer, index=None, header = None, startrow=cont, sheet_name="20_dim_US_v2")

    cont  = cont+1
    dicc = dict()
    
    
    
    
        
    
        
    
    
    