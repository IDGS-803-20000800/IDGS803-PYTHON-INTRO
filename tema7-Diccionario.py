#Las variables de tipo "diccionario" funcionan similar a los Json
miDiccionario = {"Matricula": 1234,
                 "Nombre": "Roberto",
                 "Apellidos": "Cardiel"
}

print(type(miDiccionario))
print(miDiccionario)
print(miDiccionario["Nombre"])

miDiccionario["Email"] = "rcardiel@gmail.com"
print(miDiccionario)