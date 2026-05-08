print("=== WILLIAN DEV BACKEND ACTIVADO ===")
tareas = [] 

while True:
    print("\n1. Agregar tarea")
     #backslash option + costado de 1 \\
    print("2. Ver mis tareas")
    print("3. Salir")
    opcion = input("Elije: ")

    if opcion =="1":
        nueva = input("Tarea: ")
        tareas.append(nueva)
        print(f"Guarda: {nueva}")

    elif opcion == "2":
        if len(tareas) == 0:
            print("Vacìo bro") 
        else:
            for i in range(len(tareas)):
                print(f"{i+1}. {tareas[i]}")
                #corchetes: option + costado p []

    elif opcion == "3":
        print(f"Chau. Guardaste {len (tareas)} tareas")         
        break
           



