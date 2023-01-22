print("Pedir unos números")

'''
    int : número sin punto decimal
    float : numero con punto decimal
    str : Cadena de texto

'''

num1 = int (input("Dame primer número")) #La función "input" recibe un string mediante escritura de teclado
num2 = int (input("Dame Segundo número"))

print("La suma de {} + {} = {}".format(num1, num2, (num1 + num2)))

dato1 = 100
dato2 = 23.7

print(len(str(dato1)))
print(float(dato2))