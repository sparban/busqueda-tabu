# busqueda-tabu
Programa que hace parte de la materia de optimización usando metauristicas de la maestria en computacion de la universidad del Cauca.
Se desarrollo el algoritmo de busqueda tabu, busqueda tabu con condiciones modificadas y busqueda aleatoria
Los nombres de los archivos de los algoritmos son los siguientes:

1. Busqueda Tabu original                    ----------> busqueda_tabu_original.py
2. Busqueda Tabu con condiciones modificadas ----------> busqueda_tabu_cm.py
3. Busqueda Aleatoria                        ----------> Busqueda_aleatoria.py

Se pretende evaluar la eficiencia de los algoritmos de busquedas tabu con respecto al algoritmo de busqueda aleatoria variando los siguientes parametros:

Funciones:
1. Sphere
2. Schwefel
3. Rastrigin
4. Griewank

Dimensiones de la funcion:              20, 50 y 100
Radio del Tweak:                        0.1, 0.6 y 1.0 
Numero de vecinos:                      10 y 20
Longitud de la lista (tabu original):   50, 100 y 150
Longitud de permanencia (tabu cm):      5, 10 y 15

Para la evaluacion se determina un maximo de 5000 evaluaciones maximas de la funcion objetivo o cuando el valor a minimizar sea cercano a 0.
