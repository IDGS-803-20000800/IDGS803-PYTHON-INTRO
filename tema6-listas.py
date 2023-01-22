lista1 = [1, 2, 3, 4, 5] #Forma de definir una variable de tipo lista

lista2 = [1, 3, 5, "Roberto", True]

print(lista1[-1])
print(lista1[:2])
print(lista1[1:3])
print(lista1[3:])

lista2.append("Laura") #La función "append" permite agregar un elemento al final de la lista
print(lista2)
lista2.insert(3, "Juan") #La función "insert" permite agregar un elemento en el índice indicado
print(lista2)
lista2.remove("Roberto") #La función "remove" permite eliminar los elementos que contengan el argumento indicado
print(lista2)
lista2.pop() #La función "pop" permite eliminar el último elemento de la lista
print(lista2)
del lista2[2] #La función "del" permite eliminar elementos de la lista a través de su índice
print(lista2)