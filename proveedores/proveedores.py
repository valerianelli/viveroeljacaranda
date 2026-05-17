proveedores = []
proximo_id_proveedor = 1


def registrar_proveedor():

    global proximo_id_proveedor

    nombre = input("Ingrese nombre o razón social: ")

    telefono = input("Ingrese teléfono: ")

    email = input("Ingrese email: ")

    localidad = input("Ingrese localidad: ")

    productos = input(
        "Ingrese qué provee (separado por coma): "
    ).split(",")

    productos = [producto.strip() for producto in productos]

    fecha_ultimo_pedido = input(
        "Ingrese fecha del último pedido: "
    )

    proveedor = {
        "id": proximo_id_proveedor,
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "localidad": localidad,
        "productos": productos,
        "fecha_ultimo_pedido": fecha_ultimo_pedido
    }

    proveedores.append(proveedor)

    proximo_id_proveedor += 1

    print("Proveedor registrado correctamente.")


def listar_proveedores():

    if len(proveedores) == 0:
        print("No hay proveedores registrados.")
        return

    for proveedor in proveedores:

        print("\n----------------------")
        print(f"ID: {proveedor['id']}")
        print(f"Nombre: {proveedor['nombre']}")
        print(f"Teléfono: {proveedor['telefono']}")
        print(f"Email: {proveedor['email']}")
        print(f"Localidad: {proveedor['localidad']}")
        print(f"Productos: {', '.join(proveedor['productos'])}")
        print(f"Último pedido: {proveedor['fecha_ultimo_pedido']}")


def buscar_proveedor():

    busqueda = input(
        "Buscar por nombre o producto: "
    ).lower()

    encontrado = False

    for proveedor in proveedores:

        if (
            busqueda in proveedor["nombre"].lower()
            or
            any(
                busqueda in producto.lower()
                for producto in proveedor["productos"]
            )
        ):

            print("\n----------------------")
            print(f"ID: {proveedor['id']}")
            print(f"Nombre: {proveedor['nombre']}")
            print(f"Teléfono: {proveedor['telefono']}")
            print(f"Email: {proveedor['email']}")
            print(f"Localidad: {proveedor['localidad']}")
            print(f"Productos: {', '.join(proveedor['productos'])}")
            print(f"Último pedido: {proveedor['fecha_ultimo_pedido']}")

            encontrado = True

    if not encontrado:
        print("Proveedor no encontrado.")


def actualizar_proveedor():

    id_buscar = int(
        input("Ingrese ID del proveedor a actualizar: ")
    )

    for proveedor in proveedores:

        if proveedor["id"] == id_buscar:

            proveedor["telefono"] = input(
                "Nuevo teléfono: "
            )

            proveedor["email"] = input(
                "Nuevo email: "
            )

            proveedor["localidad"] = input(
                "Nueva localidad: "
            )

            nuevos_productos = input(
                "Nuevos productos (separados por coma): "
            ).split(",")

            proveedor["productos"] = [
                producto.strip()
                for producto in nuevos_productos
            ]

            proveedor["fecha_ultimo_pedido"] = input(
                "Nueva fecha del último pedido: "
            )

            print("Proveedor actualizado.")
            return

    print("Proveedor no encontrado.")


def eliminar_proveedor():

    id_buscar = int(
        input("Ingrese ID del proveedor a eliminar: ")
    )

    for proveedor in proveedores:

        if proveedor["id"] == id_buscar:

            proveedores.remove(proveedor)

            print("Proveedor eliminado.")
            return

    print("Proveedor no encontrado.")