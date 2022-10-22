#declaring a tuple

num = (1,2,3,4,5,6,7,8)
count = 0
while (count<9):
  print (num[count])
  count = count+1
  if count == 6:
    print("Hola mundo")
    if count == 6:
      break
print ('End of program')


## Funcion eliminar elemento de la lista con condiciones modificadas
'''
list = [1,2,3,4]
cont = 0
listaFinal = []
iteracionActual = 5
while(cont < len(list)):
  if iteracionActual - list[cont] >= 4:
    list.pop(cont)
    cont = 0
  else:
    listaFinal.append(list[cont])
    cont = cont + 1
print(listaFinal)
'''

