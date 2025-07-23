import os
from ui import rutas
from ui import students
from ui import skills

opcionesMenu = [
    'Administrar Campers',
    'Administrar Rutas',
    'Gestión de Skills',
    'Salir'
]

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== MENÚ PRINCIPAL ===")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        
        try:
            op = int(input("\nSeleccione una opción: ")) - 1
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")
            continue

        if op < 0 or op >= len(opcionesMenu):
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue

        match op:
            case 0:
                students.main_menu_campers()
            case 1:
                rutas.main_menu_rutas()           
            case 2:
                skills.main_menu_skills()
            case 3:
                print("\n¡Gracias por usar el sistema! ")
                break


