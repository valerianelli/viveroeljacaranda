def generar_id_cliente(clientes):
    if len(clientes) == 0:
        return 1
    return max(cliente["id"] for cliente in clientes) + 1


def cargar_cliente(clientes):
    print("\n--- Registrar cliente ---")

    id_cliente = generar_id_cliente(clientes)

    dni = input("DNI: ")

    for cliente in clientes:
        if cliente["dni"] == dni:
            print("Ya existe un cliente con ese DNI.")
            return

    nombre_completo = input("Nombre completo: ")
    telefono = input("Teléfono: ")

    email = input("Email opcional: ")
    if email != "" and "@" not in email:
        print("Email inválido. Debe contener '@'.")
        return

    print("Tipo de cliente:")
    print("1. Particular")
    print("2. Paisajista")
    print("3. Empresa")
    print("4. Vivero amigo")

    opcion_tipo = input("Seleccione una opción: ")

    if opcion_tipo == "1":
        tipo = "particular"
    elif opcion_tipo == "2":
        tipo = "paisajista"
    elif opcion_tipo == "3":
        tipo = "empresa"
    elif opcion_tipo == "4":
        tipo = "vivero amigo"
    else:
        print("Opción incorrecta.")
        return

    notas = input("Notas: ")

    cliente = {
        "id": id_cliente,
        "dni": dni,
        "nombre_completo": nombre_completo,
        "telefono": telefono,
        "email": email,
        "tipo": tipo,
        "notas": notas
    }

    clientes.append(cliente)
    print("Cliente registrado correctamente.")


def listar_clientes(clientes):
    print("\n--- Lista de clientes ---")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print("-------------------------")
        print("ID:", cliente["id"])
        print("DNI:", cliente["dni"])
        print("Nombre completo:", cliente["nombre_completo"])
        print("Teléfono:", cliente["telefono"])
        print("Email:", cliente["email"])
        print("Tipo:", cliente["tipo"])
        print("Notas:", cliente["notas"])


def buscar_cliente_por_dni(clientes, dni):
    for cliente in clientes:
        if cliente["dni"] == dni:
            return cliente
    return None


def buscar_cliente(clientes):
    print("\n--- Buscar cliente ---")
    print("1. Buscar por DNI")
    print("2. Buscar por nombre")

    opcion = input("Seleccione una opción: ")

    encontrado = False

    if opcion == "1":
        dni = input("Ingrese DNI: ")

        for cliente in clientes:
            if cliente["dni"] == dni:
                mostrar_cliente(cliente)
                encontrado = True

    elif opcion == "2":
        nombre = input("Ingrese nombre o parte del nombre: ").lower()

        for cliente in clientes:
            if nombre in cliente["nombre_completo"].lower():
                mostrar_cliente(cliente)
                encontrado = True

    else:
        print("Opción incorrecta.")
        return

    if not encontrado:
        print("No se encontraron clientes.")


def mostrar_cliente(cliente):
    print("-------------------------")
    print("ID:", cliente["id"])
    print("DNI:", cliente["dni"])
    print("Nombre completo:", cliente["nombre_completo"])
    print("Teléfono:", cliente["telefono"])
    print("Email:", cliente["email"])
    print("Tipo:", cliente["tipo"])
    print("Notas:", cliente["notas"])


def modificar_cliente(clientes):
    print("\n--- Modificar cliente ---")

    dni = input("Ingrese el DNI del cliente a modificar: ")
    cliente = buscar_cliente_por_dni(clientes, dni)

    if cliente is None:
        print("No se encontró un cliente con ese DNI.")
        return

    while True:
        print("\n¿Qué dato desea modificar?")
        print("1. Nombre completo")
        print("2. Teléfono")
        print("3. Email")
        print("4. Tipo de cliente")
        print("5. Notas")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cliente["nombre_completo"] = input("Nuevo nombre completo: ")
            print("Nombre modificado correctamente.")
            break

        elif opcion == "2":
            cliente["telefono"] = input("Nuevo teléfono: ")
            print("Teléfono modificado correctamente.")
            break

        elif opcion == "3":
            nuevo_email = input("Nuevo email: ")

            if nuevo_email != "" and "@" not in nuevo_email:
                print("Email inválido. Debe contener '@'.")
            else:
                cliente["email"] = nuevo_email
                print("Email modificado correctamente.")
                break

        elif opcion == "4":
            print("Tipo de cliente:")
            print("1. Particular")
            print("2. Paisajista")
            print("3. Empresa")
            print("4. Vivero amigo")

            opcion_tipo = input("Seleccione una opción: ")

            if opcion_tipo == "1":
                cliente["tipo"] = "particular"
                print("Tipo modificado correctamente.")
                break
            elif opcion_tipo == "2":
                cliente["tipo"] = "paisajista"
                print("Tipo modificado correctamente.")
                break
            elif opcion_tipo == "3":
                cliente["tipo"] = "empresa"
                print("Tipo modificado correctamente.")
                break
            elif opcion_tipo == "4":
                cliente["tipo"] = "vivero amigo"
                print("Tipo modificado correctamente.")
                break
            else:
                print("Opción incorrecta. Intente nuevamente.")

        elif opcion == "5":
            cliente["notas"] = input("Nuevas notas: ")
            print("Notas modificadas correctamente.")
            break

        elif opcion == "0":
            print("Modificación cancelada.")
            break

        else:
            print("Opción incorrecta. Intente nuevamente.")


def eliminar_cliente(clientes):
    print("\n--- Eliminar cliente ---")

    dni = input("Ingrese el DNI del cliente a eliminar: ")
    cliente = buscar_cliente_por_dni(clientes, dni)

    if cliente is None:
        print("No se encontró un cliente con ese DNI.")
        return

    mostrar_cliente(cliente)

    confirmacion = input("¿Está seguro que desea eliminar este cliente? s/n: ")

    if confirmacion.lower() == "s":
        clientes.remove(cliente)
        print("Cliente eliminado correctamente.")
    else:
        print("Eliminación cancelada.")
