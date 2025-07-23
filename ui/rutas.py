import datamodels.modelsdata as models
import os

opcionesRutas = ['Crear ruta', 'Editar ruta', 'Eliminar ruta', 'Listar rutas', 'Salir']

def main_menu_rutas():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== MENÚ DE RUTAS ===")
        for i, opcion in enumerate(opcionesRutas, start=1):
            print(f"{i}. {opcion}")
        
        try:
            op = int(input("\nSeleccione una opción: ")) - 1
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")
            continue
        
        if op < 0 or op >= len(opcionesRutas):
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue
        
        match op:
            case 0:  # Crear ruta
                add_ruta()
                input("Presione Enter para continuar...")
            case 1:  # Editar ruta
                edit_ruta()
                input("Presione Enter para continuar...")
            case 2:  # Eliminar ruta
                delete_ruta()
                input("Presione Enter para continuar...")
            case 3:  # Listar rutas
                list_rutas()
                input("Presione Enter para continuar...")
            case 4:  # Salir
                print("Regresando al menú principal...")
                break

def add_ruta():
    print("\n=== CREAR NUEVA RUTA ===")
    id = str(len(models.rutas) + 1).zfill(4)
    print(f'ID asignado: {id}')
    
    nombre_ruta = input("Ingrese el nombre de la ruta: ").strip()
    if not nombre_ruta:
        print("Nombre no válido.")
        return
    
    ruta = {
        id: {
            "nombre_ruta": nombre_ruta,
            "skills": {}
        }
    }
    models.rutas.update(ruta)
    print(f"Ruta agregada exitosamente: {models.rutas[id]}")

def edit_ruta():
    print("\n=== EDITAR RUTA ===")
    if not models.rutas:
        print("No hay rutas registradas.")
        return

    print("\n--- RUTAS DISPONIBLES ---")
    for id, data in models.rutas.items():
        print(f"{id}: {data['nombre_ruta']}")

    id = input("\nIngrese el ID de la ruta que desea editar: ").strip()
    if id not in models.rutas:
        print("ID no encontrado.")
        return

    print(f"Ruta actual: {models.rutas[id]['nombre_ruta']}")
    nuevo_nombre = input("Ingrese el nuevo nombre de la ruta: ").strip()
    if not nuevo_nombre:
        print("Nombre no válido.")
        return

    models.rutas[id]['nombre_ruta'] = nuevo_nombre
    print(f"Ruta actualizada: {models.rutas[id]}")

def delete_ruta():
    print("\n=== ELIMINAR RUTA ===")
    if not models.rutas:
        print("No hay rutas registradas.")
        return

    print("\n--- RUTAS DISPONIBLES ---")
    for id, data in models.rutas.items():
        print(f"{id}: {data['nombre_ruta']}")

    id = input("\nIngrese el ID de la ruta que desea eliminar: ").strip()
    if id not in models.rutas:
        print("ID no encontrado.")
        return

    print(f"Ruta seleccionada: {models.rutas[id]['nombre_ruta']}")
    confirm = input("¿Está seguro que desea eliminar esta ruta? (s/n): ").lower().strip()
    
    if confirm == 's' or confirm == 'si':
        nombre_eliminada = models.rutas[id]['nombre_ruta']
        del models.rutas[id]
        print(f"Ruta '{nombre_eliminada}' eliminada correctamente.")
    else:
        print("Eliminación cancelada.")

def list_rutas():
    print("=== RUTAS REGISTRADAS ===")
    if not models.rutas:
        print("No hay rutas registradas.")
        return

    print(f"\nTotal de rutas: {len(models.rutas)}")
    print("-" * 40)
    for id, data in models.rutas.items():
        print(f"ID: {id} | Nombre: {data['nombre_ruta']}")
        if data['skills']:
            print(f"  Skills: {len(data['skills'])} registradas")
        else:
            print("  Skills: Ninguna registrada")
        print("-" * 40)