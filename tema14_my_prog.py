def tem():
    print("!Hola desde my_prog.py!")

def tem2():
    print("!Adios desde my_prog.py!")

def main():
    print("Soy una función y hago algo!")

    tem()
    tem2()

#La siguiente instrucción evita que se ejecuten las funciones que no pertenecen a la función main
if __name__ == "__main__":
    main()