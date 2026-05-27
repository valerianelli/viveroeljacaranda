from datetime import datetime

proximo_id_proveedor = 1

def validar_fecha(fecha_str):
    """Valida que la fecha tenga el formato DD/MM/AAAA."""
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def registrar_proveedor(lista_proveedores):
    global proximo_id_proveedor

    nombre = input("Ingrese nombre o razón social: ").strip()
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese nombre o razón social: ").strip()

    # Validación de Teléfono (solo números)
    telefono = input("Ingrese teléfono: ").strip()
    while not telefono.isdigit():
        print("Error: El teléfono debe contener solo números.")
        telefono = input("Ingrese teléfono: ").strip()

    # Validación de Email (debe contener '@')
    email = input("Ingrese email: ").strip()
    while "@" not in email:
        print("Error: El email debe contener un '@'.")
        email = input("Ingrese email: ").strip()

    localidad = input("Ingrese localidad: ").strip()

    productos = input("Ingrese qué provee (separado por coma): ").split(",")
    productos = [producto.strip() for producto in productos if producto.strip()]

    # Validación de Fecha (Formato DD/MM/AAAA)
    fecha_ultimo_pedido = input("Ingrese fecha del último pedido (DD/MM/AAAA): ").strip()
    while not validar_fecha(fecha_ultimo_pedido):
        print("Error: Formato de fecha inválido. Debe ser DD/MM/AAAA.")
        fecha_ultimo_pedido = input("Ingrese fecha del último pedido (DD/MM/AAAA): ").strip()

    proveedor = {
        "id": proximo_id_proveedor,
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "localidad": localidad,
        "productos": productos,
        "fecha_ultimo_pedido": fecha_ultimo_pedido
    }

    lista_proveedores.append(proveedor)
    proximo_id_proveedor += 1
    print("Proveedor registrado correctamente.")


def listar_proveedores(lista_proveedores):
    if len(lista_proveedores) == 0:
        print("No hay proveedores registrados.")
        return

    for proveedor in lista_proveedores:
        print("\n----------------------")
        print(f"ID: {proveedor['id']}")
        print(f"Nombre: {proveedor['nombre']}")
        print(f"Teléfono: {proveedor['telefono']}")
        print(f"Email: {proveedor['email']}")
        print(f"Localidad: {proveedor['localidad']}")
        print(f"Productos: {', '.join(proveedor['productos'])}")
        print(f"Último pedido: {proveedor['fecha_ultimo_pedido']}")


def buscar_proveedor(lista_proveedores):
    busqueda = input("Buscar por nombre o producto: ").lower().strip()
    encontrado = False

    for proveedor in lista_proveedores:
        if (
            busqueda in proveedor["nombre"].lower()
            or any(busqueda in producto.lower() for producto in proveedor["productos"])
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


def actualizar_proveedor(lista_proveedores):
    try:
        id_buscar = int(input("Ingrese ID del proveedor a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    for proveedor in lista_proveedores:
        if proveedor["id"] == id_buscar:
            
            # Teléfono nuevo (validado)
            tel = input("Nuevo teléfono: ").strip()
            while not tel.isdigit():
                print("Error: El teléfono debe contener solo números.")
                tel = input("Nuevo teléfono: ").strip()
            proveedor["telefono"] = tel

            # Email nuevo (validado)
            correo = input("Nuevo email: ").strip()
            while "@" not in correo:
                print("Error: El email debe contener un '@'.")
                correo = input("Nuevo email: ").strip()
            proveedor["email"] = correo

            proveedor["localidad"] = input("Nueva localidad: ").strip()

            nuevos_productos = input("Nuevos productos (separados por coma): ").split(",")
            proveedor["productos"] = [p.strip() for p in nuevos_productos if p.strip()]

            # Fecha nueva (validada)
            fecha = input("Nueva fecha del último pedido (DD/MM/AAAA): ").strip()
            while not validar_fecha(fecha):
                print("Error: Formato inválido. Debe ser DD/MM/AAAA.")
                fecha = input("Nueva fecha del último pedido (DD/MM/AAAA): ").strip()
            proveedor["fecha_ultimo_pedido"] = fecha

            print("Proveedor actualizado.")
            return

    print("Proveedor no encontrado.")


def eliminar_proveedor(lista_proveedores):
    try:
        id_buscar = int(input("Ingrese ID del proveedor a eliminar: "))
    except ValueError:
