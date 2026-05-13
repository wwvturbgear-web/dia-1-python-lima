print("== WILLIAN DEV BACKEND ACTIVADO - DÍA 8 ==")
import random

ARCHIVO ="tareas.txt"

def cargar_tareas():
    """Carga las tareas desde el archivo al iniciar"""
    try:
        with open(ARCHIVO, "r", encoding="uf-8") as f:
            return [linea.strip() for linea in f.readlines()]
    except FileNotFoundError:
        return []

def guardar_tareas(lista):
    """Guarda las tareas en el archivo cada vez que cambian"""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for tarea in lista:
            f.write(tarea + "\n")

def tarea_sorpresa():
    opciones = [
        "Hacer 10 flexiones",
        "Tomar agua",
        "Ordenar tu escritorio por 2 minutos",
        "Estudiar python 5 min",
        "Salir a estirarte"
    ]     
    return random.choice(opciones)
def mostrar_tareas(lista):
    if not lista:
        print("No tienes tareas. ")
    else:
        for i, tarea in enumerate(lista, 1):
            print(f"{i}. {tarea}")

def agregar_tarea(lista):
    nueva = input("Tarea: ")
    lista.append(nueva)
    guardar_tareas(lista)
    print(f"Guardada: {nueva}")

def eliminar_tarea(lista):
    mostrar_tareas(lista)
    if not lista:
        return

    try:
        num = int(input("Numero de la tarea a eliminar: ")) 
        if 1 <= num <= len(lista):
            tarea_eliminada = lista.pop(num -1 )
            guardar_tareas(lista)
            print(f"Tarea ‘{tarea_eliminada}‘ eliminada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Ingresa un número válido.")
    #cargar tareas al iniciar
tareas = cargar_tareas()

while True:
    print("\n1. Agregar tareas")
    print("2. Ver mis tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    print("5. Tarea sorpresa")

    opcion = input("Elije: ")

    if opcion == "1":
        agregar_tarea(tareas)
    elif opcion == "2":
        mostrar_tareas(tareas)
    elif opcion == "3":
        eliminar_tarea(tareas)
    elif opcion == "4":  
        print("Chau bro, nos vemos mañana")
        break
    elif opcion == "5":
        nueva_tarea = tarea_sorpresa()
        tareas.append(nueva_tarea)      
        guardar_tareas(tareas)
        print(f"¡Te tocó! Agregada: {nueva_tarea}")
    else:
        print("Opcion inválida")

