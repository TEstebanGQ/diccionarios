import os
import datamodels.modelsdata as models

opcionesSkills = [
    'Crear Skill',
    'Editar Skill',         # Pendiente de implementación
    'Eliminar Skill',       # Pendiente de implementación
    'Listar Skill',         # Pendiente de implementación
    'Salir'
]

def main_menu_skills():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Menú de Gestión de Skills ===\n")
        for i, opcion in enumerate(opcionesSkills, start=1):
            print(f"{i}. {opcion}")
        
        try:
            op = int(input("\nSeleccione una opción: ")) - 1
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")
            continue

        if op < 0 or op >= len(opcionesSkills):
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue

        match op:
            case 0:  # Crear Skill
                add_skill()
                input("Presione Enter para continuar...")
            case 1 | 2 | 3:  # No implementados aún
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
            case 4:  # Salir
                break

def add_skill():
    skill = {
        "nombre": "",
        "proyectos": {"nota": 0.0},
        "examenes": {"nota": 0.0},
        "actividades": {
            "notas": {
                "quices": [],
                "retos": [],
                "tarea": []
            }
        }
    }

    id = str(len(models.skills) + 1).zfill(4)
    print(f'\nID asignado a la nueva skill: {id}')
    
    nombre = input("Ingrese el nombre de la skill: ").strip()
    if not nombre:
        print("Nombre no válido.")
        return

    skill["nombre"] = nombre
    models.skills[id] = skill
    print(f"\n✅ Skill agregada con éxito: {models.skills[id]}")
