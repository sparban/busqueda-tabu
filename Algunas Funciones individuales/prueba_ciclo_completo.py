ListaR = [0.2, 0.6, 1.0] # paso del tweak  (0.2, 06, 1.0)
ListaN = [10, 20]  # numero de vecinos  (10, 20)
ListaTabu = [50, 100, 150] # longitud de la lista tabu  (50, 100, 150)

for tw in range (len(ListaR)):
    for vecinos in range (len(ListaN)):
        for long in range(len(ListaTabu)):
            nomenclaturaHoja = "20_dim_"+ str(ListaR[tw]) + "tw_" + str(ListaN[vecinos])+"ve_"+str(ListaTabu[long])+"longlist"
            print(nomenclaturaHoja)
            r = ListaR[tw]
            n = ListaN[vecinos]
            longitudListaTabu = ListaTabu[long]
            

            
            