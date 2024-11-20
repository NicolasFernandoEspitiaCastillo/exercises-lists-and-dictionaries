## Ejercicio 6

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
# Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la 
# lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el 
# usuario tiene que repetir.

import json
asignaturas = ["matematicas", "fisica", "quimica", "Historia", "Lengua"]
ruta_json = "exercises-lists-and-dictionaries/baseDeDatos/bdEjercicioSeis.json"


for asignatura in asignaturas[:]:  
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    if nota >= 5: 
        asignaturas.remove(asignatura)

with open (ruta_json, "w") as archivo:
    json.dump(asignaturas, archivo)

print(f"Asignaturas que tienes que repetir:")
print(", ".join(asignaturas))
