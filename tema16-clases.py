class padre():
    x = 1

#Para la herencia de clase se pone el nombre de una clase en los parentésis de otra
class operasbas(padre):
    #Definir propiedades de clase
    num1 = 0
    num2 = 0
    res = 0

    #Definir constructor de clase
    def __init__(self, a, c): #El argumento self hace referencia a la clase misma
        self.num1 = a
        self.num2 = c

    #Definimos los métodos de la clase
    def suma(self, a, b):
        self.num1 = a
        self.num2 = b
        return a + b

def main():
    #Instancia de una clase
    obj = operasbas()
    obj.suma
    print(obj.res)