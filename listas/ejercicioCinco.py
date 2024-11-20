# Ejercicio 5

# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por 
# pantalla en orden inverso separados por comas.

import json 
ruta_json = "exercises-lists-and-dictionaries/baseDeDatos/bdEjercicioCinco.json"
numeros = list(range(1, 11))
print(", ".join(map(str, numeros[::-1])))

with open (ruta_json, "w") as archivo:
    json.dump(numeros, archivo)