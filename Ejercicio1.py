num = int (input("Dame un número"))

def tablasMultiplicar(num):
    cont = 1
    while cont <=10:
        resultado = num*cont
        print("{} x {} = {}".format(num, cont, resultado))
        cont+=1

tablasMultiplicar(num)