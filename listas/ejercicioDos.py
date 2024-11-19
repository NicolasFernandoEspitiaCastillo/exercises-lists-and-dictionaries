# Ejercicio 2

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla el mensaje `Yo estudio <asignatura>`, donde `<asignatura>` 
# es cada una de las asignaturas de la lista.

import json
def Dos():
    asignaturas = [] 
    cantidad = int(input("¿Cuántas materias quieres ingresar? ")) 
    ruta_json = "/home/camper/Escritorio/exercises-lists-and-dictionaries/baseDeDatos/bdEjercicioDos.json"

    for i in range(cantidad):
        materia = input("Escribe el nombre de la materia: ")
        asignaturas.append(materia) 
    
    for asignatura in asignaturas:
        print(f"Yo estudio {asignatura}")
    
    
    with open(ruta_json, "w") as archivo:
        json.dump(asignaturas, archivo)  

    print(f"Las asignaturas se han guardado correctamente en '{ruta_json}'.")

Dos()
