
#lista de 20 posiciones, agregar a la lista numeros aleatorios entre 1 y 200

import random
numeros = random.randint(1,200)
lista = []

for i in range (21):
    numeros = random.randint(1,200)
    # que no aparezcan numeros duplicados
    if numeros not in lista:
        lista.append(numeros)
        lista.sort()

#longitud = len,,, while list len <21 ... 
#len(lista)


print(lista)