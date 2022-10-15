# Implemtacione de Funciones
import numpy as np
import pandas as pd
import random
import math

# Genero el vector solucion de forma aleatoria
s = []
for i in range(4):
    s.append(round(random.uniform(-5.12,5.12),2))      
print("Vector solucion inicial:", s)



# Funcion Multimodal separable( MS) | Rastrigin [-5.12, 5.12]
def multimodalSeparable(s):
    y = 0
    for i in range(0,len(s)):
        #print("Coseno :",10*math.cos(2*math.pi*s[i]))
        y = ((s[i])**2 -10*math.cos(2*math.pi*s[i]) + 10) + y
        print("Iteracion:",(i+1)," valor de la Funcion: ",y)
    
    return y

print("F(x) de la funcion multidomal separable Rastrigin: ",multimodalSeparable(s))



# Funcion Multimodal  No separable| Griewank [-600, 600]
def multimodalNoSeparable(s):
    #d = [5,4,2,3]
    # Variables de control
    pt_g = 0
    st_g = 1
    for i in range(0,len(s)):
        #print("Variables i-esima: ",i+1)
        pt_g = (1/4000)* s[i] + pt_g
        #p =  math.cos(d[i])/math.sqrt(i+1)
        #print("Pruebas coseno: ",p)
        st_g = (math.cos(s[i])/math.sqrt(i+1))*st_g
        #y = a -b +1

    # Se define la funcion objetivo Multimodadl No Separable (MN) - Griewank
    y = pt_g - st_g +1
    return y

print(" F(x) de la Funcion multimodal no separable (Griewank): ",multimodalNoSeparable(s))