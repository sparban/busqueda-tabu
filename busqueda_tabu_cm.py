from random import random
import random
from math import dist
import math
import pandas as pd
import numpy as np

# Definimos las variables iniciales
#==============================================================================
excel = "resultados_tabu_CM_100dim_funsion4.xlsx" # Nombre del archivo excel donde se guardan los resultados
nDim = 100 # numero de dimensiones de la funsion  (20, 50, 100)
listaLongitudPermanencia = [5, 10, 15] # longitud de la lista tabu  (50, 100, 150)
ListaN = [10, 20]  # numero de vecinos  (10, 20)
ListaR = [0.2, 0.6, 1.0] # paso del tweak  (0.2, 06, 1.0)

NMEFO = 5000  # Maximo numero de evaluaciones de la funcion objetivo

seleccion = 4
rango = 600 # rango funcion de evaluacion
# 1. Funcion Unimodal Separable | Sphere                [-100, 100]
# 2. Funcion unimodal No Separable | Schwefel           [-100, 100]
# 3. Funcion Multimodal separable( MS) | Rastrigin      [-5.12, 5.12]
# 4. Funcion Multimodal No Separable (MNS) | Griewank   [-600, 600]

# Definicion de las Funciones Objetivo
# ================================================================================

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
def vectorSolution(nDim, rango):
    s= []
    for i in range(nDim):
        s.append(random.uniform(-rango,rango))     
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

# Funcion para aplicar tweak
def aplicar_tweck (s,tw, ListaCaractersiticas, numCarModificar):
    Generaltwick = []
    listaProbabillidad = GenerarVectorProbabilidad(s, ListaCaractersiticas, numCarModificar)
    for i in range(len(s)):
        if listaProbabillidad[i] > 0.5:
            Generaltwick.append(s[i]+tw[i])
        else:
            Generaltwick.append(s[i])
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

# Funcion de creacion del indice de las condiciones modificadas

def lista_caracteristicas_modificadas(lista1):
    lista2 = []
    for i in range(len(lista1)):
        for j in range(len(lista1[i])):
            lista2.append(lista1[i][j])
    return lista2

# funcion de probabilidad

def GenerarVectorProbabilidad(s, ListaCaractersiticas, numCarModificar):
    numberDim = list(range(len(s)))
    # Se crea el vector de probabilidads de ceros proporcional al  tamaño de las dimensiones
    probabilidades = np.zeros(len(numberDim))
    # Se eliminan del vector dimensiones, las caracteriticas a no modificar.
    for i in range(len(ListaCaractersiticas)):
        numberDim.remove(ListaCaractersiticas[i])

    CaractersiticasCambiar = np.random.choice(numberDim, numCarModificar, False)

    # Remplzamos las caracteriticas a cambiar vector de probabilidades (caracteristicas 1 : cambiaron)
    for j in range(len(CaractersiticasCambiar)):
            probabilidades[CaractersiticasCambiar[j]]= 1

    return list(probabilidades)

# Evaluacion del algoritmo
#=====================================================================================

for tw in range (len(ListaR)):
    for vecinos in range (len(ListaN)):
        for long in range(len(listaLongitudPermanencia)):
            nomenclaturaHoja = str(nDim)+"_dim_"+ str(ListaR[tw]) + "tw_" + str(ListaN[vecinos])+"ve_"+str(listaLongitudPermanencia[long])+"longlist"

            contador = 1
            dicc = dict()
            r = ListaR[tw]
            n = ListaN[vecinos]
            longitudPermanencia = listaLongitudPermanencia[long]

            for z in range(0,30):
                s = []                              
                listaCaracteristicas = []           
                listaCondicionesModificadas = []
                C = 0   
                contEvaluacion = 0  
                iteracionActual = 0
                s = vectorSolution(nDim, rango)
                best = s

                calidadParada = funciones_matematicas(seleccion, s, contEvaluacion)
                QS = calidadParada[0]
                contEvaluacion = calidadParada[1]

                QBest = QS
            
                numCarModificar = int(len(s)/longitudPermanencia)

                while QBest > 1:

                    # Evaluamos ls iteracion mayor que 1
                    #================================================================================
                    if iteracionActual > 0:
                        iteracionActual += 1
                        listaCondicionesModificadas = []
                        cont = 0
                        while (cont < len(listaCaracteristicas)):
                            # Eliminamos vectores que no sombrepasaen el tiempo de longitud de permanencia
                            if iteracionActual - listaCaracteristicas[cont][1] >= longitudPermanencia:
                                listaCaracteristicas.pop(cont)
                                cont = 0
                            else:
                                listaCondicionesModificadas.append(listaCaracteristicas[cont][0])
                                cont += 1
                        # Lista de las caracteristicas modificadas
                        listaCaraModi=lista_caracteristicas_modificadas(listaCondicionesModificadas)
                        tw_R = genracionTW (s)
                        R=aplicar_tweck(s, tw_R, listaCaraModi, numCarModificar)
                        # Calculamos calidad de R
                        calidadParada = funciones_matematicas(seleccion, R, contEvaluacion)
                        QR = calidadParada[0]
                        contEvaluacion = calidadParada[1]
                        if contEvaluacion == NMEFO:
                            break

                        # Generamos los vecinos
                        for i in range(0,n-1):
                            tw_W = genracionTW(s)
                            # Aplicamos Twick a W
                            W = aplicar_tweck(s, tw_W, listaCaraModi, numCarModificar)
                            # Evaluammos W
                            calidadParada = funciones_matematicas(seleccion, W, contEvaluacion)
                            QW = calidadParada[0]
                            contEvaluacion = calidadParada[1]
                            if contEvaluacion == NMEFO:
                                break   
                            if (QW<QR):
                                R = W
                                QR = QW
                        if contEvaluacion == NMEFO:
                            break
                        ListaTupla =  creacion_tuplas(s,R,iteracionActual)   
                        listaCaracteristicas.append(ListaTupla)
                        s = R
                        QS = QR
                        if QS < QBest:
                            Best = s
                            QBest = QS
                            
                    # Evaluamos la primera iteracion
                    #================================================================================
                    else:
                        iteracionActual += 1
                        tw_R = genracionTW (s)
                        R=aplicar_tweck(s, tw_R, listaCaracteristicas, numCarModificar)
                        # Calculamos calidad de R
                        calidadParada = funciones_matematicas(seleccion, R, contEvaluacion)
                        QR = calidadParada[0]
                        contEvaluacion = calidadParada[1]
                        # Generamos los vecinos
                        for i in range(0,n-1):
                            tw_W = genracionTW(s)
                            # Aplicamos Twick a W
                            W = aplicar_tweck(s, tw_W, listaCaracteristicas, numCarModificar)
                            # Evaluammos W
                            calidadParada = funciones_matematicas(seleccion, W, contEvaluacion)
                            QW = calidadParada[0]
                            contEvaluacion = calidadParada[1]
                            if contEvaluacion == NMEFO:
                                break   
                            if (QW<QR):
                                R = W
                                QR = QW
                        ListaTupla =  creacion_tuplas(s,R,iteracionActual)   
                        listaCaracteristicas.append(ListaTupla)
                        s = R
                        QS = QR
                        if QS < QBest:
                            Best = s
                            QBest = QS
                print("Best Final iteracion: ",z," Calidad Best: ",QBest)
                # Guardamos los resultados en el excel para posteriores analisis
                # ==============================================================================
                dicc = {"Best": Best,
                        "Qbest": QBest}

                df = pd.DataFrame([[dicc[key]] for key in dicc.keys()])
                df = df.transpose()

                with pd.ExcelWriter(excel,engine="openpyxl", mode = 'a', if_sheet_exists="overlay"
                                    ) as writer:
                    df.to_excel(writer, index=None, header = None, startrow=contador, sheet_name=nomenclaturaHoja)

                contador  = contador+1
                dicc = dict()
