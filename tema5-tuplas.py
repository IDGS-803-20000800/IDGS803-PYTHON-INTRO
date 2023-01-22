tupla = (1, 2, 3, 4)

print(type(tupla))
print(tupla)

tupla2 = (7, "Roberto", True, 23.9, 12 + 3j)
print(tupla2)

tupla3 = tupla + tupla2
print(tupla3)
print(tupla2[1]) #Los corchetes sirven para indicar que quieres extraer el objeto del índice indicado
print(tupla2[:]) #Los ":" indican que quieres obtener toda la tupla
print(tupla2[:4]) #El índice después de los ":" indica que quieres obtener todo hasta antes de la posición indicada
print(tupla2[2:]) #El índice antes de los ":" indica que quieres obtener todo lo que esta después de la posición indicada
print(tupla2[-1]) #Un índice negativo extraera los datos de manera inversa, es decir, comenzando por el último dato
print(tupla2[-2])