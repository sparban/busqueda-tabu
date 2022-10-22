from math import dist
import random
s = []
p = []
numDimensiones = 5
# Creacion de las funciones objetivos (solucion inicial propuesta)
for i in range(numDimensiones):
    s.append(round(random.uniform(-100,100),2))      
print("Vector s:", s)

for i in range(numDimensiones):
    p.append(round(random.uniform(-100,100),2))      
print("Vector p:", p)

print(dist(s,p))

# Funcion calculo distancias euclidianas
def funcion_distancia_euclidiana (L, listaEvaluacion):
    ListaDistanciasEuclidianas = []
    for i in range (len(L)):
        ListaDistanciasEuclidianas.append(dist(L[i],listaEvaluacion))
    return ListaDistanciasEuclidianas