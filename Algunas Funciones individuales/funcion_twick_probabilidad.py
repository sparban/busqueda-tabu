import random
s = []
r = 0.2
numDimensiones = 5

def genracionTW (s):
    tw = []
    for i in range(len(s)):
        tw.append(random.uniform(-r,r))
    return tw

def funcion_probabilidad (s,r):
    probabilidad = []
    for i in range(len(s)):
        probabilidad.append(random.uniform(0,1))
    return probabilidad

for i in range(numDimensiones):
    s.append(round(random.uniform(-100,100),2))      
print("Vector solucion inicial:", s)

# Generacion del twick
tw_W = genracionTW (s)
print(f"Tw de R: {tw_W}")

W = []

listaProbabillidad = funcion_probabilidad(s,r)

print(f"Lista de probabilidades {listaProbabillidad}")

# funcion de evaluacion del twick
for i in range(len(s)):
    if listaProbabillidad[i] > 0.5:
        W.append(s[i]+tw_W[i])
    else:
        W.append(s[i])

print(f"Vector W: {W}")
