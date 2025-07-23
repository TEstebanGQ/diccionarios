from ui import mainmenu

if __name__ == "__main__":
    mainmenu.main_menu()
    
                
    # st.add_student()
    # # print(models.campus)
    # # st.show_students()
    # os.system('cls' if os.name == 'nt' else 'clear')
    # id = input("Ingrese el ID del Estudiante a mostrar: ")
    # student = models.campus.get(id, {})
    # print("Rutas Disponibles:")
    # print("Seleccione una ruta a matricular")
    # opciones = list(models.rutas.keys())
    # for i, opcion in enumerate(opciones, start=1):
    #     print(f"{i}. {opcion}")

    # opcion = int(input("Ingrese el número de la ruta: ")) - 1
    # models.rutas.get(opcion,-1)

    # ruta = {
    #     "nombre_ruta": opciones[opcion],
    #     "skills": {}
    # }
    # student.update({"ruta": ruta})
    # print(models.campus)