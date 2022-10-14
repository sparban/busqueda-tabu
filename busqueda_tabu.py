# Busqueda tabu

from random import random
import random
import numpy as np

l = 50 # nlongi
n = 10
r = 0.2 # paso del tweak
rango = [-100, 100]
s = []

# Creacion de las funciones objetivos

# 

for i in range(20):
    s.append(round(random.uniform(-100,100),2))      
print("Vector solucion inicial:", s)

# lista tabu
# agregamos el s a la lista tabu

L = []
L.append(s)   # aguegamos la solucion inicial S a la lista tabu

# Evaluamos la funcion objetivo

# Funcion de calidad (Unimodal Separable)

def unimodalNoSeparable (s): 
    y = 0
    for i in range(len(s)):
        y = round((s[i]*s[i]) + y, 2)
    return y

# Funcion de evaluacion (unimodal no separable)

def unimodalNoSeparable(s):
    acum = 0
    y =0
    for i in range(len(s)):
        acum = (s[i]+acum)
        y = acum*acum + y
    return(y)



best = s

for i in range(1,100):

    QS = unimodalNoSeparable(s)
    print("Calidad de S: ", QS)
    
    QBest = unimodalNoSeparable(best)
    print("Calidad de best: ", QBest)

    print("Lista tabu: ", L)
    
        
    # Generamos el tweak

    def genracionTW (s):
        tw = []
        for i in range(len(s)):
            tw.append(random.randint(-1,1)*r)
        return tw

    # Aplicamos el tweak al vector solucion

    R = []
    tw_R = genracionTW (s)
    print(f"Tw de R: {tw_R}")
    for i in range(len(s)):
        R.append(s[i]+tw_R[i])

    print(f"Vector R: {R}")

    QR = unimodalNoSeparable(R)
    print(f"calidad de R: {QR}")

    W = []

    for i in range(0,n-1):
        print("----------------------------------------------------------")
        tw_W = genracionTW(s)
        print(f"Tw de W: {tw_W}")
        for i in range(len(s)):
            W.append(s[i]+tw_W[i])
        
        print(f"Vector W: {W}")
        
        # Evaluammos W
        
        QW = unimodalNoSeparable(W)
        print(f"calidad de W: {QW}")
        
        if (not(W in L) and (QW>QR)) or (R in L):
            R = W
            print("Se cumple")
        W = []
        
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
        