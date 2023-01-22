dato1 = "Hola"
dato2 = "Mundo"

datoFinal = dato1 + " " + dato2
print(datoFinal)

#Se pueden concatenar datos utilizando el operador de "%" e indicando con "%s" donde van dichos datos
print("El saludo es: %s %s" %(dato1, dato2))

#Al añadir llaves en una cadena, se usa la función "format" para poder indicar los datos que se van a agregar
saludo = "Saludo2 {0} {1}".format(dato1, dato2)

print(saludo)

#Se pueden cambiar el orden en que aparecen los argumentos en las llaves mediante un índice
saludo = "Saludo2 {1} {0}".format(dato1, dato2)

print(saludo)