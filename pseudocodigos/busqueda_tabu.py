# Algoritmo busqueda Tabu
longitud Lista Tabu                 L               #Logitud Permanecia Lista
numero Vecinos                      N               #Numero de vecino
paso Twick                          R               #pasoTwick   
numero Dimenciones                  ndim            #Numero de dimenciones   
MaximoNumeroEvalucacioFO            NMEFO           #maximo numero Evaluaciones
Rango                               rangoF          #Rango donde se evalua la funcion objetivo
Seleccion                           selec           #Seleccion de la variable deacuerdo Tipo de Funcion
Contador NMFO                       contEvaluacion  #Contador que aumenta a medida que aumenta la evaluacion de la funcion objetivo

# Definicion de las caracteristicas iniciales
s <-- vectorSolution(nDim)
Best <-- s
Qs = funciones_matematicas(seleccion, s, contEvaluacion)
QBest = Qs
contEvaluacion = 0                   
Agrego s in L 

# Flujo General

Repetir
     
    tw_R <--  generacionTW(s)
    R <-- aplicar_tweck(s, tw_R)
    QR, contEvaluacion <-- funciones_matematicas(seleccion, R, contEvaluacion)
    if contEvaluacion == NMEFO entonces
        terminar proceso
    for N-1 veces hacer:
        tw_W  <-- genracionTW(s)
        W <-- aplicar_tweck(s, tw_W)
        QW, contEvaluacion <-- funciones_matematicas(seleccion, W, contEvaluacion)
        if contEvaluacion == NMEFO entonces
            terminar proceso
        
        distanciaEuclidoanaR <---- funcion_distancia_euclidiana(L, R) #calcular distancia euclidiana de R con cada elemento de L
        distanciaEuclidoanaW <---- funcion_distancia_euclidiana(L, W) #calcular distancia euclidiana de W con cada elemento de L
        distanciaEuclidoanaR <---- comprobar_distancia_euclidiana(distanciaEuclidoanaR, 0.2) # Evaluamos si R esta en L por medio de las distancias Eu
        distanciaEuclidoanaW <---- comprobar_distancia_euclidiana(distanciaEuclidoanaW, 0.2) # Evaluamos si W esta en L por medio de las distancias EU
        
        if W no pertenece a L and QW < QR or R pertenece a L entonces:
            R <-- W
            QR <-- QW
            
        distanciaEuclidoanaR <---- funcion_distancia_euclidiana(L, R) #calcular distancia euclidiana de R con cada elemento de L
        distanciaEuclidoanaR <---- comprobar_distancia_euclidiana(distanciaEuclidoanaR, 0.2) # Evaluamos si R esta en L por medio de las distancias Eu
        
    if R no pertenece a L y QW < QS entonces:
        s <-- R
        Qs <-- QR
        Agrego R en L
    if Qs < Qbest entinces:
        Best <-- s
        QBest <-- Qs
        
Hasta Best sea la solucion ideal o NMEFO = 5000
Return Best, Qbest