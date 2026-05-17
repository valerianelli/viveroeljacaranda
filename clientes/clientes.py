clientes = []
proximo_id_cliente = 1


def pedir_dni():
    dni = input("Ingrese DNI: ")

    while not dni.isdigit():
        print("Error: el DNI debe contener solo números.")
        dni = input("Ingrese DNI nuevamente: ")

    return dni


def pedir_email():
    email = input("Ingrese email (opcional): ")

    while email != "" and "@" not in email:
        print("Error: el email debe contener @ o dejarse vacío.")
        email = input("Ingrese email nuevamente: ")

    return email


def pedir_tipo_cliente():
    print("\nTipos de cliente permitidos:")
    print("1. Particular")
    print("2. Paisajista")
    print("3. Empresa")
    print("4. Vivero amigo")

    opcion = input("Ingrese una opción: ")

    while opcion not in ["1", "2", "3", "4"]:
        print("Error: opción incorrecta.")
        opcion = input("Ingrese una opción nuevamente: ")

    match opcion:
        case "1":
            return "particular"
        case "2":
            return "paisajista"
        case "3":
            return "empresa"
        case "4":
            return "vivero amigo"


def existe_dni(dni):
    for cliente in clientes:
        if cliente["dni"] == dni:
            return True

    return False


def buscar_cliente_por_dni(dni):
    for cliente in clientes:
        if cliente["dni"] == dni:
            return cliente

    return None


def mostrar_cliente(cliente):
    print("\n--- DATOS DEL CLIENTE ---")
    print(f"ID: {cliente['id']}")
    print(f"DNI: {cliente['dni']}")
    print(f"Nombre: {cliente['nombre']}")
    print(f"Teléfono: {cliente['telefono']}")
    print(f"Email: {cliente['email']}")
    print(f"Tipo: {cliente['tipo']}")
    print(f"Notas: {cliente['notas']}")
    print("--------------------------")


def cargar_cliente():
    global proximo_id_cliente

    dni = pedir_dni()

    if existe_dni(dni):
        print("Error: ya existe un cliente cargado con ese DNI.")
        return

    nombre = input("Ingrese nombre completo: ")
    telefono = input("Ingrese teléfono: ")
    email = pedir_email()
    tipo = pedir_tipo_cliente()
    notas = input("Ingrese notas del cliente: ")

    cliente = {
        "id": proximo_id_cliente,
        "dni": dni,
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "tipo": tipo,
        "notas": notas
    }

    clientes.append(cliente)
    proximo_id_cliente += 1

    print("Cliente cargado correctamente.")


def listar_clientes():
    if len(clientes) == 0:
        print("No hay clientes cargados.")
        return

    print("\n--- LISTADO DE CLIENTES ---")

    for cliente in clientes:
        mostrar_cliente(cliente)


def buscar_cliente():
    if len(clientes) == 0:
        print("No hay clientes cargados.")
        return

    dato_busqueda = input("Ingrese DNI o nombre del cliente a buscar: ").lower()

    encontrado = False

    for cliente in clientes:
        dni = cliente["dni"].lower()
        nombre = cliente["nombre"].lower()

        if dato_busqueda in dni or dato_busqueda in nombre:
            mostrar_cliente(cliente)
            encontrado = True

    if not encontrado:
        print("No se encontró ningún cliente con ese dato.")


def modificar_cliente():
    if len(clientes) == 0:
        print("No hay clientes cargados.")
        return

    dni_buscar = input("Ingrese el DNI del cliente que desea modificar: ")

    cliente = buscar_cliente_por_dni(dni_buscar)

    if cliente is None:
        print("No se encontró ningún cliente con ese DNI.")
        return

    mostrar_cliente(cliente)

    print("\n¿Qué dato desea modificar?")
    print("1. DNI")
    print("2. Nombre")
    print("3. Teléfono")
    print("4. Email")
    print("5. Tipo de cliente")
    print("6. Notas")
    print("7. Cancelar")

    opcion = input("Ingrese una opción: ")

    match opcion:
        case "1":
            nuevo_dni = pedir_dni()

            if nuevo_dni == cliente["dni"]:
                print("El DNI ingresado es el mismo que ya tenía el cliente.")
            elif existe_dni(nuevo_dni):
                print("Error: ya existe otro cliente cargado con ese DNI.")
            else:
                cliente["dni"] = nuevo_dni
                print("DNI actualizado correctamente.")

        case "2":
            cliente["nombre"] = input("Ingrese nuevo nombre completo: ")
            print("Nombre actualizado correctamente.")

        case "3":
            cliente["telefono"] = input("Ingrese nuevo teléfono: ")
            print("Teléfono actualizado correctamente.")

        case "4":
            cliente["email"] = pedir_email()
            print("Email actualizado correctamente.")

        case "5":
            cliente["tipo"] = pedir_tipo_cliente()
            print("Tipo de cliente actualizado correctamente.")

        case "6":
            cliente["notas"] = input("Ingrese nuevas notas: ")
            print("Notas actualizadas correctamente.")

        case "7":
            print("Modificación cancelada.")

        case _:
            print("Opción incorrecta.")


def eliminar_cliente():
    if len(clientes) == 0:
        print("No hay clientes cargados.")
        return

    dni_buscar = input("Ingrese el DNI del cliente que desea eliminar: ")

    cliente = buscar_cliente_por_dni(dni_buscar)

    if cliente is None:
        print("No se encontró ningún cliente con ese DNI.")
        return

    mostrar_cliente(cliente)

    confirmacion = input("¿Está seguro que desea eliminar este cliente? (s/n): ").lower()

    if confirmacion == "s":
        clientes.remove(cliente)
        print("Cliente eliminado correctamente.")
    else:
        print("Eliminación cancelada.")
