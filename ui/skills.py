import os
import datamodels.modelsdata as models

opcionesSkills = [
    'Crear Skill',
    'Editar Skill',         
    'Eliminar Skill',       
    'Listar Skill',         
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
            case 0:  
                add_skill()
                input("Presione Enter para continuar...")
            case 1:  
                edit_skill()
                input("Presione Enter para continuar...")
            case 2:  
                delete_skill()
                input("Presione Enter para continuar...")
            case 3:  
                list_skills()
                input("Presione Enter para continuar...")
            case 4:  
                break

def add_skill():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== CREAR NUEVA SKILL ===")
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
    print(f'ID asignado a la nueva skill: {id}')
    
    nombre = input("Ingrese el nombre de la skill: ").strip()
    if not nombre:
        print("Nombre no válido.")
        return

    skill["nombre"] = nombre
    models.skills[id] = skill
    print(f"Skill agregada con éxito: {models.skills[id]['nombre']}")

def edit_skill():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== EDITAR SKILL ===")
    
    # CORRECCIÓN: Verificar models.skills en lugar de models.rutas
    if not models.skills:
        print("No hay skills registradas.")
        return
    
    print("\n--- SKILLS DISPONIBLES ---")
    # CORRECCIÓN: Mostrar skills en lugar de rutas
    for id, data in models.skills.items():
        print(f"{id}: {data['nombre']}")
    
    id = input("\nIngrese el ID de la skill a editar: ").strip()
    
    if id not in models.skills:
        print("ID no encontrado.")
        return

    skill = models.skills[id]
    print(f"\nSkill actual: {skill['nombre']}")
    
    nuevo_nombre = input("Ingrese el nuevo nombre de la skill: ").strip()
    if not nuevo_nombre:
        print('Nombre no válido.')
        return

    skill['nombre'] = nuevo_nombre
    models.skills[id] = skill
    print(f"Skill actualizada: {models.skills[id]['nombre']}")

def delete_skill():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== ELIMINAR SKILL ===")
    
    # CORRECCIÓN: Verificar models.skills en lugar de models.rutas
    if not models.skills:
        print("No hay skills registradas.")
        return
    
    print("\n--- SKILLS DISPONIBLES ---")
    # CORRECCIÓN: Mostrar skills en lugar de rutas
    for id, data in models.skills.items():
        print(f"{id}: {data['nombre']}")
    
    id = input("Ingrese el ID de la skill a eliminar: ").strip()
    
    if id not in models.skills:
        print("ID no encontrado.")
        return

    # Mostrar información antes de eliminar
    skill_nombre = models.skills[id]['nombre']
    confirm = input(f"¿Está seguro de eliminar la skill '{skill_nombre}'? (s/n): ").strip().lower()
    
    if confirm == 's' or confirm == 'si':
        del models.skills[id]
        print(f"Skill '{skill_nombre}' eliminada exitosamente.")
    else:
        print("Eliminación cancelada.")

def list_skills():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=== LISTA DE SKILLS ===")
    
    if not models.skills:
        print("No hay skills registradas.")
        return

    print(f"\nTotal de skills: {len(models.skills)}")
    print("-" * 50)
    
    for id, skill in models.skills.items():
        print(f"ID: {id}")
        print(f"  └─ Nombre: {skill['nombre']}")
        print(f"  └─ Proyectos: {skill['proyectos']['nota']}")
        print(f"  └─ Exámenes: {skill['examenes']['nota']}")
        
        
        actividades = skill['actividades']['notas']
        quices = len(actividades['quices'])
        retos = len(actividades['retos'])
        tareas = len(actividades['tarea'])
        
        print(f"  └─ Actividades: {quices} quices, {retos} retos, {tareas} tareas")
        print("-" * 50)