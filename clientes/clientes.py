from ventas.visualizacion import mostrar_ventas
from encargos.encargos import buscar_por_cliente
from encargos.menu_encargos import mostrar_encargo

def generar_id_cliente(clientes):
    if len(clientes) == 0:
        return 1
    return max(cliente["id"] for cliente in clientes) + 1


def pedir_dni():
    dni = input("DNI: ")

    while not dni.isdigit():
        print("Error: el DNI debe contener solo números.")
        dni = input("Ingrese DNI nuevamente: ")

    return dni


def pedir_nombre_completo():
    nombre = input("Nombre completo: ")

    while nombre.strip() == "":
        print("Error: el nombre no puede quedar vacío.")
        nombre = input("Ingrese nombre completo nuevamente: ")

    return nombre


def pedir_telefono():
    telefono = input("Teléfono: ")

    while not telefono.isdigit():
        print("Error: el teléfono debe contener solo números.")
        telefono = input("Ingrese teléfono nuevamente: ")

    return telefono


def pedir_email():
    email = input("Email opcional: ")

    while email != "" and "@" not in email:
        print("Error: email inválido. Debe contener '@' o dejarse vacío.")
        email = input("Ingrese email nuevamente: ")

    return email


def pedir_tipo_cliente():
    opcion_tipo = ""

    while opcion_tipo not in ["1", "2", "3", "4"]:
        print("\nTipo de cliente:")
        print("1. Particular")
        print("2. Paisajista")
        print("3. Empresa")
        print("4. Vivero amigo")

        opcion_tipo = input("Seleccione una opción: ")

        if opcion_tipo not in ["1", "2", "3", "4"]:
            print("Error: opción incorrecta. Vuelva a intentarlo.")

    match opcion_tipo:
        case "1":
            return "particular"
        case "2":
            return "paisajista"
        case "3":
            return "empresa"
        case "4":
            return "vivero amigo"


def pedir_confirmacion():
    confirmacion = input("¿Está seguro que desea eliminar este cliente? s/n: ").lower()

    while confirmacion not in ["s", "n"]:
        print("Error: debe ingresar 's' para sí o 'n' para no.")
        confirmacion = input("Ingrese nuevamente s/n: ").lower()

    return confirmacion


def buscar_cliente(clientes, ventas, plantas, encargos):
    print("\n--- Buscar cliente ---")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    opcion = ""

    while opcion not in ["1", "2"]:
        print("1. Buscar por DNI")
        print("2. Buscar por nombre")

        opcion = input("Seleccione una opción: ")

        if opcion not in ["1", "2"]:
            print("Error: opción incorrecta. Vuelva a intentarlo.")

    encontrado = False

    if opcion == "1":
        dni = pedir_dni()

        for cliente in clientes:
            if cliente["dni"] == dni:
                mostrar_cliente(cliente)
                _mostrar_historial(cliente, ventas, plantas, encargos)
                encontrado = True

    elif opcion == "2":
        nombre = input("Ingrese nombre o parte del nombre: ").lower()

        while nombre.strip() == "":
            print("Error: debe ingresar un nombre o parte del nombre.")
            nombre = input("Ingrese nombre o parte del nombre nuevamente: ").lower()

        for cliente in clientes:
            if nombre in cliente["nombre_completo"].lower():
                mostrar_cliente(cliente)
                _mostrar_historial(cliente, ventas, plantas, encargos)
                encontrado = True

    if not encontrado:
        print("No se encontraron clientes.")

def buscar_cliente_por_dni(clientes, dni):
    for cliente in clientes:
        if cliente["dni"] == dni:
            return cliente
    return None

def existe_dni(clientes, dni):
    return buscar_cliente_por_dni(clientes, dni) is not None


def mostrar_cliente(cliente):
    print("-------------------------")
    print("ID:", cliente["id"])
    print("DNI:", cliente["dni"])
    print("Nombre completo:", cliente["nombre_completo"])
    print("Teléfono:", cliente["telefono"])
    print("Email:", cliente["email"])
    print("Tipo:", cliente["tipo"])
    print("Notas:", cliente["notas"])


def _mostrar_historial(cliente, ventas, plantas, encargos):
    id_cliente = cliente["id"]

    print("\n--- COMPRAS ANTERIORES DEL CLIENTE ---")
    mostrar_ventas(ventas, plantas, id_cliente)

    print("\n--- ENCARGOS ACTIVOS DEL CLIENTE ---")

    encargos_cliente = buscar_por_cliente(encargos, id_cliente)

    hay_encargos_activos = False

    for encargo in encargos_cliente:
        estado = encargo["estado"].lower()

        if estado != "entregado" and estado != "cancelado":
            mostrar_encargo(encargo)
            hay_encargos_activos = True

    if not hay_encargos_activos:
        print("El cliente no tiene encargos activos.")

def cargar_cliente(clientes):
    print("\n--- Registrar cliente ---")

    id_cliente = generar_id_cliente(clientes)

    dni = pedir_dni()

    while existe_dni(clientes, dni):
        print("Error: ya existe un cliente con ese DNI.")
        dni = pedir_dni()

    nombre_completo = pedir_nombre_completo()
    telefono = pedir_telefono()
    email = pedir_email()
    tipo = pedir_tipo_cliente()
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
        mostrar_cliente(cliente)


def modificar_cliente(clientes):
    print("\n--- Modificar cliente ---")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    dni = pedir_dni()
    cliente_encontrado = buscar_cliente_por_dni(clientes, dni)

    if cliente_encontrado is None:
        print("Cliente no encontrado.")
        return

    seguir_modificando = True

    while seguir_modificando:
        mostrar_cliente(cliente_encontrado)

        print("\n--- MODIFICAR CLIENTE ---")
        print("1. DNI")
        print("2. Nombre")
        print("3. Teléfono")
        print("4. Email")
        print("5. Tipo")
        print("6. Notas")
        print("0. Finalizar modificación")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nuevo_dni = pedir_dni()

        match opcion:
            case "1":
                nuevo_dni = pedir_dni()
                while nuevo_dni != cliente_encontrado["dni"] and existe_dni(clientes, nuevo_dni):
                    print("Error: ya existe otro cliente con ese DNI.")
                    nuevo_dni = pedir_dni()

                if nuevo_dni == cliente_encontrado["dni"]:
                    print("El DNI ingresado es el mismo que ya tenía el cliente.")
                else:
                    cliente_encontrado["dni"] = nuevo_dni
                    print("DNI actualizado.")

            case "2":
                cliente_encontrado["nombre_completo"] = pedir_nombre_completo()
                print("Nombre actualizado.")

            case "3":
                cliente_encontrado["telefono"] = pedir_telefono()
                print("Teléfono actualizado.")

            case "4":
                cliente_encontrado["email"] = pedir_email()
                print("Email actualizado.")

            case "5":
                cliente_encontrado["tipo"] = pedir_tipo_cliente()
                print("Tipo actualizado.")

            case "6":
                cliente_encontrado["notas"] = input("Ingrese nuevas notas: ")
                print("Notas actualizadas.")

            case "0":
                print("Modificación finalizada.")
                seguir_modificando = False

            case _:
                print("Opción incorrecta. Vuelva a ingresar una opción.")


def eliminar_cliente(clientes):
    print("\n--- Eliminar cliente ---")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    dni = pedir_dni()
    cliente = buscar_cliente_por_dni(clientes, dni)

    if cliente is None:
        print("No se encontró un cliente con ese DNI.")
        return

    mostrar_cliente(cliente)

    confirmacion = pedir_confirmacion()

    if confirmacion == "s":
        clientes.remove(cliente)
        print("Cliente eliminado correctamente.")
    else:
        print("Eliminación cancelada.")
