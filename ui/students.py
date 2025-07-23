import datamodels.modelsdata as models
import os
import ui.mainmenu as mainmenu
opcionesCampers = ['Crear camper','Editar camper','Eliminar camper','Listar campers','Salir']
def main_menu_campers()-> int:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bienvenido al Menú de Campers")
    for i, opcion in enumerate(opcionesCampers, start=1):
        print(f"{i}. {opcion}")
    try:
        op = int(input("Seleccione una opción: ")) - 1
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        input("Presione Enter para continuar...")
        return main_menu_campers()
    if op < 0 or op >= len(opcionesCampers):
        print("Opción no válida. Intente de nuevo.")
        return main_menu_campers()
    match op:
        case 0:  # Crear camper
            add_student()
            input("Presione Enter para continuar...")
            return main_menu_campers()
        case 1:  # Editar camper
            pass
        case 2:  # Eliminar camper
            pass
        case 3:  # Listar campers
            show_students()
            input("Presione Enter para continuar...")   
            return main_menu_campers()
        case 4:  # Salir
            mainmenu.main_menu()
        case _:
            print("Opción no implementada aún.")
            input("Presione Enter para continuar...")
            return main_menu_campers()


def add_student():
    os.system('cls' if os.name == 'nt' else 'clear')

    student = models.students.copy()
    id = input("Ingrese el ID del Estudiante: ")
    student['nombre'] = input("Ingrese el Nombre del Estudiante: ")
    student['edad'] = int(input("Ingrese la Edad del Estudiante: "))
    student['email'] = input("Ingrese el Email del Estudiante: ")
    student['telefono'] = input("Ingrese el Telefono del Estudiante: ")
    models.campus.update({id: student})

def show_students():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Lista de Estudiantes:")
    for id, student in models.campus.items():
        print(f'ID: {id}, Nombre: {student['nombre']}, Edad: {student['edad']}, Email: {student['email']}, Telefono: {student['telefono']}')