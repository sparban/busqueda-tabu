import random

# Condicion de evaluacion (almacenar)
contEvaluacion = 0
s = []
# definimos el vector soluciion  inicial 
for i in range(10):
    s.append(round(random.uniform(-100,100),2))      
print("Vector solucion inicial:", s)



def unimodalSeparable(s, contEvaluacion, ):
    acum = 0
    y =0
    contEvaluacion += 1
    for i in range(len(s)):
        acum = (s[i]+acum)
        y = acum*acum + y
    return(y, contEvaluacion)

for iteracion in range (5):
    
    calidadParada = unimodalSeparable(s, contEvaluacion)
    QS = calidadParada[0]
    contEvaluacion = calidadParada[1]
print("Contados condicion de evaluacion: ", QS, contEvaluacion)