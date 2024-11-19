## Ejercicio 3

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura, y 
# después las muestre por pantalla con el mensaje `En <asignatura> has sacado <nota>` 
# donde `<asignatura>` es cada una des las asignaturas de la lista y `<nota>` cada una de las correspondientes notas introducidas por el usuario.

import json
def tres():
    cantidad = int(input("Ingrese la cantidad de asignaturas: "))
    asignaturas = ["matematicas", "fisica", "quimica", "historia"]

    bdEjercicioTres = {}
    
    for asignatura in range(0, cantidad):
        notas = int(input(f"¿Qué nota sacó en {asignaturas[asignatura]}?: "))
        bdEjercicioTres [asignaturas[asignatura]] = notas
        print(f"En {asignaturas[asignatura]} has sacado, {notas}")
    
    ruta_json = "/home/camper/Escritorio/exercises-lists-and-dictionaries/baseDeDatos/bdEjercicioTres.json"
    
    
    with open(ruta_json, "w") as archivo:
        json.dump(bdEjercicioTres, archivo)
        print("Las notas se han guardado correctamente en 'notas_asignaturas.json'.")

tres()

