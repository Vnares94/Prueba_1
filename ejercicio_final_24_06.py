import traceback

# Funciones de ingreso con validaciones
def ingreso_direccion(contacto):
    while True:
        direccion = input(f"Ingrese la dirección del contacto {contacto}: ").strip()
        if len(direccion) > 60:
            print("Debe ingresar una dirección de hasta 60 caracteres.")
            continue
        return direccion

def ingreso_correo(contacto):
    while True:
        correo = input(f"Ingrese el correo electrónico del contacto {contacto}: ").strip()
        if correo.count("@") != 1 or "." not in correo.split("@")[-1]:
            print("El correo debe tener 1 arroba y un dominio válido.")
            continue
        if len(correo) > 50:
            print("Debe ingresar un correo de hasta 50 caracteres.")
            continue
        return correo

def ingreso_numero(contacto):
    while True:
        try:
            telefono = int(input(f"Ingrese el número telefónico de 7 dígitos del contacto {contacto}: "))
            if 1000000 <= telefono <= 9999999:
                return telefono
            else:
                print("Debe ingresar un número de exactamente 7 dígitos.")
        except ValueError:
            print("Ingrese un número válido.")

def ingreso_contacto():
    while True:
        contacto = input("Ingresa el nombre del contacto: ").strip()
        if len(contacto) == 0:
            print("El nombre no puede estar vacío.")
            continue
        if len(contacto) > 50:
            print("Debe ingresar un nombre de hasta 50 caracteres.")
            continue
        if contacto in libreta_contactos:
            print("Ya existe un contacto con este nombre. Ingrese uno diferente.")
            continue
        return contacto

def mostrar_contacto(nombre, datos):
    print(f"Nombre: {nombre}")
    print(f"Teléfono: {datos['telefono']}")
    print(f"Dirección: {datos['direccion']}")
    print(f"Correo: {datos['correo']}\n")

# Variables principales
libreta_contactos = {}
sw = True

# Menú principal
while sw:
    try:
        print("--- Menú Principal ---")
        print("1.- Crear contacto")
        print("2.- Modificar contacto")
        print("3.- Eliminar contacto")
        print("4.- Listar contactos")
        print("5.- Buscar contactos")
        print("6.- Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            contacto = ingreso_contacto()
            telefono = ingreso_numero(contacto)
            direccion = ingreso_direccion(contacto)
            correo = ingreso_correo(contacto)
            libreta_contactos[contacto] = {
                "telefono": telefono,
                "direccion": direccion,
                "correo": correo
            }
            print("Contacto agregado exitosamente.\n")

        elif opcion == "2":
            if not libreta_contactos:
                print("No hay contactos registrados.\n")
                continue
            contacto = input("Ingrese el nombre del contacto a modificar: ").strip()
            if contacto not in libreta_contactos:
                print("No se encontró ningún contacto con ese nombre.\n")
                continue

            print("Opciones de modificación:")
            print("1.- Nombre")
            print("2.- Teléfono")
            print("3.- Dirección")
            print("4.- Correo")
            print("5.- Volver")

            while True:
                op_mod = input("Seleccione una opción: ").strip()
                if op_mod == "1":
                    nuevo_nombre = ingreso_contacto()
                    libreta_contactos[nuevo_nombre] = libreta_contactos.pop(contacto)
                    print("Nombre actualizado correctamente.\n")
                    break
                elif op_mod == "2":
                    libreta_contactos[contacto]["telefono"] = ingreso_numero(contacto)
                    print("Teléfono actualizado correctamente.\n")
                    break
                elif op_mod == "3":
                    libreta_contactos[contacto]["direccion"] = ingreso_direccion(contacto)
                    print("Dirección actualizada correctamente.\n")
                    break
                elif op_mod == "4":
                    libreta_contactos[contacto]["correo"] = ingreso_correo(contacto)
                    print("Correo actualizado correctamente.\n")
                    break
                elif op_mod == "5":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")

        elif opcion == "3":
            if not libreta_contactos:
                print("No hay contactos registrados.\n")
                continue
            contacto = input("Ingrese el nombre del contacto a eliminar: ").strip()
            if contacto not in libreta_contactos:
                print("No se encontró ningún contacto con ese nombre.\n")
                continue
            confirmacion = input(f"¿Está seguro que desea eliminar a {contacto}? (s/n): ").strip().lower()
            if confirmacion == "s":
                libreta_contactos.pop(contacto)
                print("Contacto eliminado.\n")
            else:
                print("Operación cancelada.\n")

        elif opcion == "4":
            if not libreta_contactos:
                print("No hay contactos registrados.\n")
                continue
            print("\n--- Lista de Contactos ---")
            for i, contacto in enumerate(sorted(libreta_contactos), start=1):
                print(f"Contacto #{i}")
                mostrar_contacto(contacto, libreta_contactos[contacto])

        elif opcion == "5":
            if not libreta_contactos:
                print("No hay contactos registrados.\n")
                continue

            print("Opciones de búsqueda:")
            print("1.- Por nombre")
            print("2.- Por teléfono")
            print("3.- Por dirección")
            print("4.- Por correo")
            print("5.- Volver")

            while True:
                busqueda = input("Seleccione una opción: ").strip()

                if busqueda == "1":
                    nombre = input("Ingrese el nombre a buscar: ").strip()
                    if nombre in libreta_contactos:
                        print("\nContacto encontrado:")
                        mostrar_contacto(nombre, libreta_contactos[nombre])
                    else:
                        print("No se encontró el contacto.\n")

                elif busqueda == "2":
                    try:
                        telefono = int(input("Ingrese el número de 7 dígitos: "))
                        encontrado = False
                        for contacto, datos in libreta_contactos.items():
                            if datos["telefono"] == telefono:
                                print("Contacto encontrado:")
                                mostrar_contacto(contacto, datos)
                                encontrado = True
                                break
                        if not encontrado:
                            print("No se encontró ningún contacto con ese número.\n")
                    except ValueError:
                        print("Número inválido.\n")

                elif busqueda == "3":
                    direccion = input("Ingrese la dirección a buscar: ").strip()
                    encontrado = False
                    for contacto, datos in libreta_contactos.items():
                        if datos["direccion"] == direccion:
                            print("Contacto encontrado:")
                            mostrar_contacto(contacto, datos)
                            encontrado = True
                            break
                    if not encontrado:
                        print("No se encontró ningún contacto con esa dirección.\n")

                elif busqueda == "4":
                    correo = input("Ingrese el correo a buscar: ").strip()
                    encontrado = False
                    for contacto, datos in libreta_contactos.items():
                        if datos["correo"] == correo:
                            print("Contacto encontrado:")
                            mostrar_contacto(contacto, datos)
                            encontrado = True
                            break
                    if not encontrado:
                        print("No se encontró ningún contacto con ese correo.\n")

                elif busqueda == "5":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "6":
            print("Gracias por usar la aplicación. Adiós.")
            sw = False

        else:
            print("Opción inválida. Intente nuevamente.\n")

    except Exception as e:
        print("Ocurrió un error inesperado:")
        traceback.print_exc()
