## Ejercicio 8

#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

# Un palíndromo es una palabra, frase o número que se lee igual de izquierda a derecha que de 
# derecha a izquierda. En este caso, vamos a escribir un programa en Python que
# verifique si una palabra ingresada por el usuario es un palíndromo.


import json
ruta_json = "exercises-lists-and-dictionaries/baseDeDatos/bdEjercicioOcho.json"
palabra = input("Introduce una palabra: ")

if palabra == palabra[::-1]:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")

with open (ruta_json, "w") as archivo:
    json.dump(palabra, archivo)

