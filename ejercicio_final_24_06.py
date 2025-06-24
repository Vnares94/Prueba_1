# VERSIÓN P R E L I M I N A R

# Definición de funciones
def ingreso_direccion(contacto):
    while True:
        direccion = input(f"Ingrese la dirección del contacto {contacto}: ")
        if len(direccion) > 60:
            print("Debe ingresar una dirección de hasta 60 caracteres.")
            continue
        return direccion
    
def ingreso_correo(contacto):
    while True:
        correo = input(f"Ingrese el correo electrónico del contacto {contacto}: ")
        chequeo_arrobas = correo.count("@")
        if chequeo_arrobas != 1:
            print("El correo debe tener 1 arroba.")
            continue
        if len(correo) > 50:
            print("Debe ingresar un correo de hasta 50 caracteres.")
            continue
        return correo
    
def ingreso_numero(contacto):
    while True:
        try:
            telefono = int(input(f"Ingrese el número telefónico de 7 dígitos del contacto {contacto}: "))
            if telefono < 1000000 or telefono > 9999999:
                print("Respuesta inválida. Deben ser 7 dígitos.")
                continue
            return telefono
        except ValueError:
            print("Ingrese un número válido.")

def ingreso_contacto():
    while True:
        contacto = input("Ingresa el nombre del contacto: ")
        if len(contacto) > 50:
            print("Debe ingresar un nombre de contacto de hasta 50 caracteres.")
            continue
        if contacto in libreta_contactos:
            print("Ya existe un contacto con este nombre. Ingrese un nombre válido.\n")
            continue
        return contacto

# Declaración de variables
sw = True
libreta_contactos = {}
op = ""
telefono = 0
direccion = ""
correo = ""
op_mod = ""
op_elim = ""

# Ejecución
while sw: # Menú principal
    try: 
        print("---Menú---")
        print("1.- Crear contacto.")
        print("2.- Modificar contactos.")
        print("3.- Eliminar contactos.")
        print("4.- Listar contactos.")
        print("5.- Buscar contactos.")
        print("6.- Salir.")

        op = input("Ingrese una opción: ")

        if op == "1": # Crear contacto
            contacto = ingreso_contacto()
            telefono = ingreso_numero(contacto)
            direccion = ingreso_direccion(contacto)
            correo = ingreso_correo(contacto)
            libreta_contactos[contacto] = [telefono, direccion, correo]
            print("Contacto agregado exitosamente. \n")

        elif op == "2": # Modificar contacto
            if len(libreta_contactos) == 0:
                print("No se registran contactos.\n")
                continue
            contacto = input("Ingrese el nombre del contacto que desea modificar: ")
            if contacto not in libreta_contactos:
                print("No se registra ningún contacto con ese nombre. Operación cancelada.\n")
                continue
            print("\nOpciones de modificación: ")
            print("1.- Nombre de contacto")
            print("2.- Teléfono de contacto")
            print("3.- Dirección de contacto")
            print("4.- Correo de contacto")
            print("5.- Volver al menú principal")

            while True: # Menú de modificación
                op_mod = input("Ingrese una de las opciones: ")
                if op_mod == "1": # Modificar nombre de contacto
                    nuevo_contacto = ingreso_contacto()
                    libreta_contactos[nuevo_contacto] = libreta_contactos.pop(contacto)
                    print("Nombre de contacto modificado correctamente.\n")
                    break
                elif op_mod == "2": # Modificar teléfono
                    libreta_contactos[contacto][0] = ingreso_numero(contacto)
                    print("Número de contacto modificado correctamente.\n")
                    break
                elif op_mod == "3": # Modificar dirección
                    libreta_contactos[contacto][1] = ingreso_direccion(contacto)
                    print("Dirección modificada correctamente.\n")
                    break
                elif op_mod == "4": # Modificar correo
                    libreta_contactos[contacto][2] = ingreso_correo(contacto)
                    print("Correo modificado correctamente.\n")
                    break
                elif op_mod == "5": # Volver al menú principal
                    break
                else:
                    print("Ingrese una opción válida.")
                    continue
            
        elif op == "3": # Eliminar contacto
            if len(libreta_contactos) == 0:
                print("No se registran contactos.\n")
                continue
            contacto = input("Ingrese el nombre del contacto que desea eliminar: ")
            if contacto not in libreta_contactos:
                print("No se registra ningún contacto con ese nombre. Operación cancelada.\n")
                continue
            while True:
                op_elim = input(f"Confirme que desea eliminar el contacto {contacto}: (s/n)").lower()
                if op_elim == "s":
                    libreta_contactos.pop(contacto)
                    print("Contacto eliminado exitosamente.\n")
                    break
                elif op_elim == "n":
                    print("Operación cancelada.\n")
                    break
                else:
                    print("Ingrese una opción válida: (s/n).")

        elif op == "4": # Mostrar lista de contactos
            if len(libreta_contactos) == 0:
                print("No se registran contactos.\n")
                continue
            print(f"Libreta de contactos: \n")
            for i, contacto in enumerate(libreta_contactos):
                print(f"Contacto nro. {i+1}.\n {contacto}\n Teléfono: {libreta_contactos[contacto][0]}\n Dirección: {libreta_contactos[contacto][1]}\n Correo: {libreta_contactos[contacto][2]}\n")

        elif op == "5": # Buscar contactos
            if len(libreta_contactos) == 0:
                print("No se registran contactos.\n")
                continue
            
            while True: # Menú de búsqueda
                print("\nOpciones de búsqueda: ")
                print("1.- Buscar por nombre de contacto")
                print("2.- Buscar por teléfono de contacto")
                print("3.- Buscar por dirección de contacto")
                print("4.- Buscar por correo de contacto")
                print("5.- Volver al menú principal")

                op_mod = input("Ingrese una de las opciones: ")

                if op_mod == "1": # Buscar por nombre de contacto
                    contacto = input("Ingrese el nombre que desea buscar: ")
                    if contacto not in libreta_contactos:
                        print("No se ha encontrado ningún contacto con ese nombre.\n")
                        continue
                    print("Se ha encontrado el contacto. A continuación se muestra su información: ")
                    print(f"Nombre: {contacto}\n Teléfono: {libreta_contactos[contacto][0]}\n Dirección: {libreta_contactos[contacto][1]}\n Correo: {libreta_contactos[contacto][2]}\n")


                elif op_mod == "2": # Buscar por teléfono
                    while True:
                        try:
                            telefono = int(input(f"Ingrese el número telefónico de 7 dígitos que desea buscar: "))
                            if telefono < 1000000 or telefono > 9999999:
                                print("Respuesta inválida. Deben ser 7 dígitos.")
                                continue
                            break
                        except ValueError:
                            print("Ingrese un número válido.")
                    búsqueda_exitosa = False
                    for contacto in libreta_contactos:
                        if telefono == libreta_contactos[contacto][0]:
                            print(f"Se ha encontrado el número de teléfono. A continuación se muestra la información de contacto: ")
                            print(f"Nombre: {contacto}\n Teléfono: {libreta_contactos[contacto][0]}\n Dirección: {libreta_contactos[contacto][1]}\n Correo: {libreta_contactos[contacto][2]}\n")
                            busqueda_exitosa = True
                            break
                    if busqueda_exitosa == False:
                        print("No se ha encontrado ningún contacto con ese número.")

                elif op_mod == "3": # Buscar por dirección
                    direccion = input("Ingrese la dirección que desea buscar: ")
                    busqueda_exitosa = False
                    for contacto in libreta_contactos:
                        if direccion == libreta_contactos[contacto][1]:
                            print(f"Se ha encontrado la dirección. A continuación se muestra la información de contacto: ")
                            print(f"Nombre: {contacto}\n Teléfono: {libreta_contactos[contacto][0]}\n Dirección: {libreta_contactos[contacto][1]}\n Correo: {libreta_contactos[contacto][2]}\n")
                            busqueda_exitosa = True
                            break
                    if busqueda_exitosa == False:
                        print("No se ha encontrado ningún contacto con esa dirección.")

                elif op_mod == "4": # Buscar por correo
                    busqueda_exitosa = False
                    correo = input("Ingrese el correo que desea buscar: ")
                    for contacto in libreta_contactos:
                        if correo == libreta_contactos[contacto][2]:
                            print(f"Se ha encontrado el correo. A continuación se muestra la información de contacto: ")
                            print(f"Nombre: {contacto}\n Teléfono: {libreta_contactos[contacto][0]}\n Dirección: {libreta_contactos[contacto][1]}\n Correo: {libreta_contactos[contacto][2]}\n")
                            busqueda_exitosa = True
                            break
                    if busqueda_exitosa == False:
                        print("No se ha encontrado ningún contacto con esa dirección.")

                elif op_mod == "5": # Volver al menú principal
                        break
                else:
                    print("Ingrese una opción válida.")
                    continue            

        elif op == "6": # Salir de la aplicación
            print("Gracias por usar la aplicación. Adiós.")
            sw = False
            break

        else:
            print("Ingrese una opción válida.\n")
            continue
    except Exception as e:
        print(f"Error inesperado: {e}")
