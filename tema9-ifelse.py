num1 = int (input("Dame primer número")) #La función "input" recibe un string mediante escritura de teclado
num2 = int (input("Dame Segundo número"))

#La función "if" permite comparar argumentos entre sí
if(num1 > num2): #Se puede poner o no el parentésis y funciona igual
    print("{} es mayor que {}".format(num1, num2))
else:
    print("{1} es mayor que {0}".format(num1, num2))

print ("----------Dato nuevo----------")

edad = int(input("Dame tu edad"))

if edad > 18:
    print("Eres mayor de edad")
#La función "elif" sirve para anidar funciones "if" en el caso de que haya más de una comparación
elif edad == 18:
    print("Tienes 18")
else:
    print("Eres menor de edad")