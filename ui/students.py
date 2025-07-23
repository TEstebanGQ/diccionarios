import datamodels.modelsdata as models
import os
import ui.mainmenu as mainmenu
opcionesCampers = ['Crear camper','Editar camper','Eliminar camper','Listar campers','Salir']
def main_menu_campers()-> int:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenido al Menú de Campers")
        for i, opcion in enumerate(opcionesCampers, start=1):
            print(f"{i}. {opcion}")
        try:
            op = int(input("Seleccione una opción: ")) - 1
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")
            continue    
        if op < 0 or op >= len(opcionesCampers):
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue
           
        match op:
            case 0:  
                add_student()
                input("Presione Enter para continuar...")
                
            case 1:  
                edit_student()
                input("Presione Enter para continuar...")
                
            case 2:  
                delete_student()
                input("Presione Enter para continuar...")
                
            case 3:  
                show_students()
                input("Presione Enter para continuar...")   
                
            case 4:  
                mainmenu.main_menu()
            

def add_student():
    os.system('cls' if os.name == 'nt' else 'clear')

    student = models.students.copy()
    id = input("Ingrese el ID del Estudiante: ")
    student['nombre'] = input("Ingrese el Nombre del Estudiante: ")
    student['edad'] = int(input("Ingrese la Edad del Estudiante: "))
    student['email'] = input("Ingrese el Email del Estudiante: ")
    student['telefono'] = input("Ingrese el Telefono del Estudiante: ")
    models.campus.update({id: student})

def edit_student():
    os.system('cls' if os.name == 'nt' else 'clear')
    id = input("Ingrese el ID del Estudiante a editar: ")
    if id not in models.campus:
        print("ID no encontrado.")
        return
    
    student = models.campus[id]
    print(f"Estudiante actual: {student['nombre']}")
    
    student['nombre'] = input("Ingrese el nuevo nombre del estudiante: ").strip()
    if not student['nombre']:
        print("Nombre no válido.")
        return
    
    student['edad'] = int(input("Ingrese la nueva edad del estudiante: "))
    student['email'] = input("Ingrese el nuevo email del estudiante: ")
    student['telefono'] = input("Ingrese el nuevo telefono del estudiante: ")
    
    models.campus[id] = student
    print(f"Estudiante actualizado: {models.campus[id]}")

def delete_student():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not models.campus:
        print("No hay estudiantes registrados.")
        return
    
    print("--- ESTUDIANTES DISPONIBLES ---")
    for id, student in models.campus.items():
        print(f"ID: {id}, Nombre: {student['nombre']}")
    
    id = input("\nIngrese el ID del estudiante que desea eliminar: ").strip()
    if id not in models.campus:
        print("ID no encontrado.")
        return
    
    confirm = input(f"¿Está seguro de eliminar al estudiante '{models.campus[id]['nombre']}'? (s/n): ").strip().lower()
    if confirm == 's' or confirm == 'si':
        del models.campus[id]
        print("Estudiante eliminado correctamente.")
    else:
        print("Eliminación cancelada.")

def show_students():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Lista de Estudiantes:")
    for id, student in models.campus.items():
        print(f'ID: {id}, Nombre: {student['nombre']}, Edad: {student['edad']}, Email: {student['email']}, Telefono: {student['telefono']}')