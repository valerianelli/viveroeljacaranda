from datetime import datetime


def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def generar_proximo_id(lista_proveedores):

    if not lista_proveedores:
        return 1

    return max(prov["id"] for prov in lista_proveedores) + 1


def registrar_proveedor(lista_proveedores):

    nombre = input("Ingrese nombre o razón social: ").strip()
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese nombre o razón social: ").strip()

    telefono = input("Ingrese teléfono: ").strip()
    while not telefono.isdigit():
        print("Error. Solo números en teléfono.")
        telefono = input("Ingrese teléfono: ").strip()

    email = input("Ingrese email: ").strip()
    while "@" not in email:
        print("Error. Email inválido.")
        email = input("Ingrese email: ").strip()

    localidad = input("Ingrese localidad: ").strip()
    while not localidad:
        print("La localidad no puede estar vacía.")
        localidad = input("Ingrese localidad: ").strip()

    productos = [
        p.strip()
        for p in input("Productos (separados por coma): ").split(",")
        if p.strip()
    ]

    fecha = input("Fecha último pedido (DD/MM/AAAA): ").strip()
    while not validar_fecha(fecha):
        print("Fecha inválida. Debe ser DD/MM/AAAA.")
        fecha = input("Fecha último pedido (DD/MM/AAAA): ").strip()

    proveedor = {
        "id": generar_proximo_id(lista_proveedores),
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "localidad": localidad,
        "productos": productos,
        "fecha_ultimo_pedido": fecha
    }

    lista_proveedores.append(proveedor)
    print("Proveedor registrado correctamente.")


def listar_proveedores(lista_proveedores):

    if not lista_proveedores:
        print("No hay proveedores.")
        return

    for p in lista_proveedores:
        print("\n-------------------")
        print(f"ID: {p['id']}")
        print(f"Nombre: {p['nombre']}")
        print(f"Teléfono: {p['telefono']}")
        print(f"Email: {p['email']}")
        print(f"Localidad: {p['localidad']}")
        print(f"Productos: {', '.join(p['productos'])}")
        print(f"Último pedido: {p['fecha_ultimo_pedido']}")


def buscar_proveedor(lista_proveedores):
    if not lista_proveedores:
        print("No hay proveedores.")
        return

    texto = input("Buscar nombre o producto: ").lower()

    encontrado = False

    for p in lista_proveedores:

        if texto in p["nombre"].lower() or any(texto in prod.lower() for prod in p["productos"]):

            print("\n-------------------")
            print(f"ID: {p['id']}")
            print(f"Nombre: {p['nombre']}")
            print(f"Teléfono: {p['telefono']}")
            print(f"Email: {p['email']}")
            print(f"Localidad: {p['localidad']}")
            print(f"Productos: {', '.join(p['productos'])}")
            print(f"Último pedido: {p['fecha_ultimo_pedido']}")

            encontrado = True

    if not encontrado:
        print("No se encontraron resultados.")


def actualizar_proveedor(lista_proveedores):
    if not lista_proveedores:
        print("No hay proveedores.")
        return

    try:
        id_buscar = int(input("ID a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    for p in lista_proveedores:

        if p["id"] == id_buscar:

            p["telefono"] = input("Nuevo teléfono: ").strip()
            while not p["telefono"].isdigit():
                print("Error. Solo números en teléfono.")
                p["telefono"] = input("Nuevo teléfono: ").strip()

            p["email"] = input("Nuevo email: ").strip()
            while "@" not in p["email"]:
                print("Error. Email inválido.")
                p["email"] = input("Nuevo email: ").strip()

            p["localidad"] = input("Nueva localidad: ").strip()
            while not p["localidad"]:
                print("La localidad no puede estar vacía.")
                p["localidad"] = input("Nueva localidad: ").strip()

            p["productos"] = [
                x.strip()
                for x in input("Nuevos productos: ").split(",")
                if x.strip()
            ]

            fecha = input("Nueva fecha (DD/MM/AAAA): ").strip()
            while not validar_fecha(fecha):
                print("Fecha inválida. Debe ser DD/MM/AAAA.")
                fecha = input("Nueva fecha (DD/MM/AAAA): ").strip()

            p["fecha_ultimo_pedido"] = fecha

            print("Proveedor actualizado.")
            return

    print("Proveedor no encontrado.")


def eliminar_proveedor(lista_proveedores):

    if not lista_proveedores:
        print("No hay proveedores.")
        return

    try:
        id_buscar = int(input("ID a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return

    for p in lista_proveedores:

        if p["id"] == id_buscar:

            print(f"Proveedor: {p['nombre']}")
            confirmacion = input("Eliminar? (S/N): ").upper()

            if confirmacion == "S":
                lista_proveedores.remove(p)
                print("Eliminado.")
            else:
                print("Cancelado.")

            return

    print("No encontrado.")
