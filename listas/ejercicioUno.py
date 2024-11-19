# Ejercicio 1

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla.

import json
def uno():
    asignaturas = ["matematicas", "fisica", "quimica", "historia"]
    ruta_json = "/home/camper/Escritorio/exercises-lists-and-dictionaries/baseDeDatos/bdEjercicioUno.json"
   

    with open(ruta_json, "w") as archivo:
        json.dump(asignaturas, archivo)

    for asignatura in asignaturas:
        print(asignatura)

    
    print(f"Los datos se han guardado correctamente en '{ruta_json}'.")


    

uno()