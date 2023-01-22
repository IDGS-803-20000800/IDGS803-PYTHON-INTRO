def suma(num1, num2):
    resultado = num1 + num2
    return resultado

def resta(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicacion(num1, num2):
    resultado = num1 * num2
    return resultado

def division(num1, num2):
    resultado = num1 / num2
    return resultado

def main():
    print("Elige una de las siguientes opciones")
    print ("1.- Suma")
    print ("2.- Resta")
    print ("3.- Multiplicación")
    print ("4.- Division")
    print ("5.- Salir")

    opcion = int(input())

    if opcion == 1:
        numero1 = int(input("Escribe el primer número"))
        numero2 = int(input("Escribe el segundo número"))
        resultado = suma(numero1, numero2)
        print("El resultado es: " + str(resultado))

    elif opcion == 2:
        numero1 = int(input("Escribe el primer número"))
        numero2 = int(input("Escribe el segundo número"))
        resultado = resta(numero1, numero2)
        print("El resultado es: " + str(resultado))

    elif opcion == 3:
        numero1 = int(input("Escribe el primer número"))
        numero2 = int(input("Escribe el segundo número"))
        resultado = multiplicacion(numero1, numero2)
        print("El resultado es: " + str(resultado))

    elif opcion == 4:
        numero1 = int(input("Escribe el primer número"))
        numero2 = int(input("Escribe el segundo número"))
        resultado = division(numero1, numero2)
        print("El resultado es: " + str(resultado))

    else:
        print("Hasta luego")

if __name__ == "__main__":
    main()