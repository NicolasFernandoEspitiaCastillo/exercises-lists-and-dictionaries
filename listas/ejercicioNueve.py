## Ejercicio 9

#Escribir un programa que pida al usuario una palabra y muestre por pantalla 
#el número de veces que contiene cada vocal.

import json
ruta_json = "exercises-lists-and-dictionaries/baseDeDatos/bdEjercicioNueve.json"
palabra = input("Introduce una palabra: ").lower() 

vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for letra in palabra:
    if letra in vocales:
        vocales[letra] += 1

for vocal, cantidad in vocales.items():
    print(f"La vocal '{vocal}' aparece {cantidad} vez/veces.")

with open (ruta_json, "w") as archivo:
    json.dump(vocales, archivo)