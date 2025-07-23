import datamodels.modelsdata as models
import os

opcionesRutas = ['Crear ruta', 'Editar ruta', 'Eliminar ruta', 'Listar rutas', 'Salir']

def main_menu_rutas():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenido al Menú de Rutas")
        for i, opcion in enumerate(opcionesRutas, start=1):
            print(f"{i}. {opcion}")
        try:
            op = int(input("Seleccione una opción: ")) - 1
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")
            continue
        if op < 0 or op >= len(opcionesRutas):
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue
        match op:
            case 0:
                add_ruta()
                input("Presione Enter para continuar...")
            case 1:
                edit_ruta()
                input("Presione Enter para continuar...")
            case 2:
                delete_ruta()
                input("Presione Enter para continuar...")
            case 3:
                list_rutas()
                input("Presione Enter para continuar...")
            case 4:
                break

def add_ruta():
    id = str(len(models.rutas) + 1).zfill(4)
    print(f'Id: {id}')
    nombre_ruta = input("Ingrese el nombre de la ruta: ")
    ruta = {
        id: {
            "nombre_ruta": nombre_ruta,
            "skills": {}
        }
    }
    models.rutas.update(ruta)
    print(f"Ruta agregada: {models.rutas[id]}")

def edit_ruta():
    if not models.rutas:
        print("No hay rutas registradas.")
        return

    print("\n=== RUTAS DISPONIBLES ===")
    for id, data in models.rutas.items():
        print(f"{id}: {data['nombre_ruta']}")

    id = input("\nIngrese el ID de la ruta que desea editar: ").strip()
    if id not in models.rutas:
        print("ID no encontrado.")
        return

    nuevo_nombre = input("Ingrese el nuevo nombre de la ruta: ").strip()
    if not nuevo_nombre:
        print("Nombre no válido.")
        return

    models.rutas[id]['nombre_ruta'] = nuevo_nombre
    print(f"Ruta actualizada: {models.rutas[id]}")

def delete_ruta():
    if not models.rutas:
        print("No hay rutas registradas.")
        return

    print("\n=== RUTAS DISPONIBLES ===")
    for id, data in models.rutas.items():
        print(f"{id}: {data['nombre_ruta']}")

    id = input("\nIngrese el ID de la ruta que desea eliminar: ").strip()
    if id not in models.rutas:
        print("ID no encontrado.")
        return

    confirm = input(f"¿Está seguro que desea eliminar la ruta '{models.rutas[id]['nombre_ruta']}'? (s/n): ").lower()
    if confirm == 's':
        del models.rutas[id]
        print("Ruta eliminada correctamente.")
    else:
        print("Eliminación cancelada.")

def list_rutas():
    if not models.rutas:
        print("No hay rutas registradas.")
        return

    print("=== RUTAS REGISTRADAS ===")
    for id, data in models.rutas.items():
        print(f"{id}: {data['nombre_ruta']}")
    input("Presione Enter para continuar...")