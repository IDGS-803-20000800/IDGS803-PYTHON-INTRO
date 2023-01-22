texto = "universidad tecnológica de leon"

print(type(texto)) #La función "type" Devuelve el tipo de dato de una variable
print(texto.lower()) #La función "lower" Devuelve la cadena dada en minúsculas
print(texto.upper()) #La función "upper" Devuelve la cadena dada en mayúsculas
print(texto.title()) #La función "title" Devuelve la cadena dada en con la primera letra mayúscula de cada palabra
print(texto.find("de")) #La función "find" Devuelve el índice de la cadena dada
print(texto.count("a")) #La función "count" Devuelve la cuenta de los argumentos dados que existe en la cadena
texto2 = texto.replace("e", "3") #La función "replace" reemplaza los carácteres dados como primer argumento por los carácteres dados como segundo argumento
texto3 = texto.split(" ") #La función "split" Devuelve un arreglo donde separa la cadena por los carácteres indicados
print(texto2)
print(texto3)