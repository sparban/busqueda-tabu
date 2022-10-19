
# Librerias
import numpy as np

# Lista de caracteristicas de la Lista Tabu
ListaCaractersiticas = []
s = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(len(s))


def GenerarVectorProbabilidad(s,listaTabu):
    # dimensiones del la solucion inicial s=9
    numberDim = list(range(len(s)))
    print("Numero de dimensiones: ",numberDim)
    # Se crea el vector de probabilidads de ceros proporcional al  tamaño de las dimensiones
    probabilidades = np.zeros(len(numberDim))

    # Se eleiminan del vector dimensiones, las caracteriticas a no modificar.
    for i in range(len(ListaCaractersiticas)):
        numberDim.remove(ListaCaractersiticas[i])

    print("Nuvo vector Eliminadas Caracteristicas: ",numberDim)
    
    CaractersiticasCambiar = np.random.choice(numberDim, 3,False)
    # Se selcciona el nuemro de varaibles modificar decuerdo nDim/l
    print("Los numero seleccionados son: ",CaractersiticasCambiar)
    # Remplzamos las caracteriticas a cambiar vector de probabilidades (caracteristicas 1 : cambiaron)
    for j in range(len(CaractersiticasCambiar)):
            probabilidades[CaractersiticasCambiar[j]]= 1


    return list(probabilidades)


print(GenerarVectorProbabilidad(s,ListaCaractersiticas))
