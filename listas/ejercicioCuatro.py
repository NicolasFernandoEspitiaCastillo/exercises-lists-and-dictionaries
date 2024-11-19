## Ejercicio 4

# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene 
# en una lista y los muestre por pantalla ordenados de menor a mayor.

import json
def cuatro():
    loteria = []
    ganadores = int(input("Cuantos numeros son ganadores?: "))
    ruta_json = "/home/camper/Escritorio/exercises-lists-and-dictionaries/baseDeDatos/bdEjercicioCuatro.json"
    
    for i in range(ganadores):
        numero = int(input(f"Ingresa el numero {i+1}: "))
        loteria.append(numero)

        loteria_ordenados = sorted (loteria)

        with open(ruta_json, "w") as archivo:
            json.dump(loteria, archivo)  

      
        print("numeros ganadores", loteria_ordenados)
        print(f"Los numeros ganadores estan guardados en '{ruta_json}'.")
    
cuatro()




