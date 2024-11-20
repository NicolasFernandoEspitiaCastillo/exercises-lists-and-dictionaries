## Ejercicio 10

#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre
#por pantalla el menor y el mayor de los precios.

import json
ruta_json = "exercises-lists-and-dictionaries/baseDeDatos/bdEjercicioDiez.json"
precios = [50, 75, 46, 22, 80, 65, 8]

menor_precio = min(precios)
mayor_precio = max(precios)

print(f"El menor precio es: {menor_precio}")
print(f"El mayor precio es: {mayor_precio}")

with open (ruta_json, "w") as archivo:
    json.dump(precios, archivo)