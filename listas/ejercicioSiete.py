## Ejercicio 7

#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen 
#posiciones múltiplos de 3, y muestre por pantalla la lista resultante.



import json
ruta_json = "exercises-lists-and-dictionaries/baseDeDatos/bdEjercicioSiete.json"
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

abecedario_resultante = [letra for i, letra in enumerate(abecedario) if (i + 1) % 3 != 0]

with open (ruta_json, "w") as archivo:
    json.dump(abecedario_resultante, archivo)

print(abecedario_resultante)


