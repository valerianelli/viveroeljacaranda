from datetime import datetime


def validar_fecha(fecha_str):

    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True

    except ValueError:
        return False


def generar_proximo_id(lista_proveedores):

    if len(lista_proveedores) == 0:
        return 1

    id_maximo = 0

    for proveedor in lista_proveedores:
        if proveedor["id"] > id_maximo:
            id_maximo = proveedor["id"]

    return id_maximo + 1


def registrar_proveedor(lista_proveedores):

    nombre = input("Ingrese nombre o razón social: ").strip()

    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese nombre o razón social: ").strip()

    telefono = input("Ingrese teléfono: ").strip()

    while not telefono.isdigit():
        print("Error: El teléfono debe contener solo números.")
        telefono = input("Ingrese teléfono: ").strip()

    email = input("Ingrese email: ").strip()

    while "@" not in email:
        print("Error: El email debe contener un '@'.")
        email = input("Ingrese email: ").strip()

    localidad = input("Ingrese localidad: ").strip()

    productos = input(
        "Ingrese qué provee (separado por coma): "
    ).split(",")

    productos = [
        producto.strip()
        for producto in productos
        if producto.strip()
    ]

    fecha_ultimo_pedido = input(
        "Ingrese fecha del último pedido (DD/MM/AAAA): "
    ).strip()

    while not validar_fecha(fecha_ultimo_pedido):
        print("Error: Formato inválido. Debe ser DD/MM/AAAA.")
        fecha_ultimo_pedido = input(
            "Ingrese fecha del último pedido (DD/MM/AAAA): "
        ).strip()

    proveedor = {
        "id": generar_proximo_id(lista_proveedores),
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "localidad": localidad,
        "productos": productos,
        "fecha_ultimo_pedido": fecha_ultimo_pedido
    }

    lista_proveedores.append(proveedor)

    print("Proveedor registrado correctamente.")


def eliminar_proveedor(lista_proveedores):

    if not lista_proveedores:
        print("No hay proveedores registrados.")
        return

    try:
        id_buscar = int(
            input("Ingrese ID del proveedor a eliminar: ")
        )

    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return

    for proveedor in lista_proveedores:

        if proveedor["id"] == id_buscar:

            print("\nProveedor encontrado:")
            print(f"ID: {proveedor['id']}")
            print(f"Nombre: {proveedor['nombre']}")

            confirmacion = input(
                "¿Desea eliminar este proveedor? (S/N): "
            ).strip().upper()

            if confirmacion == "S":

                lista_proveedores.remove(proveedor)

                print("Proveedor eliminado correctamente.")

            else:
                print("Eliminación cancelada.")

            return

    print("Proveedor no encontrado.")
