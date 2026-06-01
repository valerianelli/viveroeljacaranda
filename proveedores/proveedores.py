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

    return max(prov["id"] for prov in lista_proveedores)


def registrar_proveedor(lista_proveedores):

    nombre = input("Ingrese nombre o razón social: ").strip()
    while not nombre:
        nombre = input("El nombre no puede estar vacío: ").strip()

    telefono = input("Ingrese teléfono: ").strip()
    while not telefono.isdigit():
        telefono = input("Error. Solo números en teléfono: ").strip()

    email = input("Ingrese email: ").strip()
    while "@" not in email:
        email = input("Error. Email inválido: ").strip()

    localidad = input("Ingrese localidad: ").strip()

    productos = [
        p.strip()
        for p in input("Productos (separados por coma): ").split(",")
        if p.strip()
    ]

    fecha = input("Fecha último pedido (DD/MM/AAAA): ").strip()
    while not validar_fecha(fecha):
        fecha = input("Fecha inválida. Reintente: ").strip()

    proveedor = {
        "id": generar_proximo_id(lista_proveedores) + 1,
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

    texto = input("Buscar nombre o producto: ").lower()

    encontrados = False

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

            encontrados = True

    if not encontrados:
        print("No se encontraron resultados.")


def actualizar_proveedor(lista_proveedores):

    try:
        id_buscar = int(input("ID a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    for p in lista_proveedores:

        if p["id"] == id_buscar:

            p["telefono"] = input("Nuevo teléfono: ").strip()
            p["email"] = input("Nuevo email: ").strip()
            p["localidad"] = input("Nueva localidad: ").strip()

            p["productos"] = [
                x.strip()
                for x in input("Nuevos productos: ").split(",")
                if x.strip()
            ]

            fecha = input("Nueva fecha (DD/MM/AAAA): ").strip()
            while not validar_fecha(fecha):
                fecha = input("Fecha inválida: ").strip()

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
