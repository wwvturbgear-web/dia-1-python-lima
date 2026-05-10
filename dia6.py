print ("== WILLIAN DEV BACKEND ACTIVADO - DÍA 6 ==")
tareas = []

def mostrar_tareas(lista):
    """Muestra todas las tareas con numeración"""
    if len(lista) == 0:
        print("Vacío bro")
    else:
        for i in range(len(lista)):
            print(f"{i+1}. {Lista[i]}")

def agregar_tarea(lista):
    """Pide una tarea y la agrega a la lista"""
    nueva = input("Tarea: ")
    lista.append(nueva)
    print(f"Guarda: {nueva}")

while True:
    print("\n1. Agregar tareas")
    print("2. Ver mis tareas")
    print("3. Salir")
    opcion = input("Elije: ")
        
    if opcion == "1":
        agregar_tarea(tareas) 

    elif opcion == "2":
        mostrar_tareas(tareas)

    elif opcion == "3":
        print("Chau bro, nos vemos mañana")
    break

else:
    print("Opción inválida")                 