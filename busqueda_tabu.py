# Busqueda tabu

from random import random
import random
#import numpy as np

l = 50 # nlongi
n = 3
r = 0.2 # paso del tweak
rango = [-100, 100]
s = []
contEvaluacion = 0   # variable para almacenar la NMEFO
NMEFO = 40  # maximo numero de evaluaciones de la funcion objetivo
# Creacion de las funciones objetivos (solucion inicial propuesta)
for i in range(5):
    s.append(round(random.uniform(-100,100),2))      
print("Vector solucion inicial:", s)

# lista tabu
# agregamos el s a la lista tabu

L = []
L.append(s)   # aguegamos la solucion inicial S a la lista tabu

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
        tw.append(random.randint(-1,1)*r)
    return tw

best = s
print(contEvaluacion)

# Condicion de evaluacion del minimo encontrado
while contEvaluacion < 100:

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
    for i in range(len(s)):
        R.append(s[i]+tw_R[i])

    print(f"Vector R: {R}")

    calidadParada = unimodalNoSeparable(R, contEvaluacion)
    QR = calidadParada[0]
    contEvaluacion = calidadParada[1]
    if contEvaluacion == NMEFO:
        break
    print(f"calidad de R:", QR, contEvaluacion)

    W = []

    # Generamos los vecinos
    for i in range(0,n-1):
        print("----------------------------------------------------------")
        tw_W = genracionTW(s)
        print(f"Tw de W: {tw_W}")
        for i in range(len(s)):
            W.append(s[i]+tw_W[i])
        
        print(f"Vector W: {W}")
        
        # Evaluammos W
        
        calidadParada = unimodalNoSeparable(W, contEvaluacion)
        QW = calidadParada[0]
        contEvaluacion = calidadParada[1]
        if contEvaluacion == NMEFO:
            break   
        print(f"calidad de W: ", QW, contEvaluacion)
        
        if (not(W in L) and (QW>QR)) or (R in L):
            R = W
            print("Se cumple")
        W = []
        
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
        