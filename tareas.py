
print ("== WILLIAN DEV BACKEND ACTIVADO - DÍA 7 ==")
tareas = []
import random
def tarea_sorpresa():
    opciones = [
        "Hacer 10 flexiones",
        "Tomar agua",
        "Ordenar tu escritorio por 2 minutos",
        "Estudiar python 5 min",
        "Salir a estirarte"
    ]
    tarea = random.choice(opciones)
    return tarea

def mostrar_tareas(lista):
    if not lista:
        print("No tienes tareas. ")
    else:
        for i in range(len(lista)):
            print(f"{i+1}. {lista[i]}")
            #cd Desktop/mi_primer_proyecto

def agregar_tarea(lista):
    nueva= input("Tarea: ")
    lista.append(nueva)
    print(f"Guarda: {nueva}")

def eliminar_tarea(lista):
    mostrar_tareas(lista)
    if not lista:
        return

    try:
        num = int(input("Numero de la tarea a eliminar: "))
        if 1 <= num <= len(lista):
             tarea_eliminada = lista.pop(num -1)
             print(f"Tarea '{tarea_eliminada}' eliminada. ")
        else:
            print("Número inválido.")        
    except ValueError:
        print("Ingresa un numero válido. ")      
tareas = []  
#option mas costado p []      
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
        print(f"¡Te tocó! Agregada: {nueva_tarea}")      
    
    else:
        print("Opción inválida")   

