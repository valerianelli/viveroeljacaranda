from .constantes import FORMAS_PAGO, parsear_fecha

# ─────────────────────────────────────────────
#  Cliente
# ─────────────────────────────────────────────


def pedir_cliente(clientes):
    """
    Solicita un DNI y retorna el id del cliente si existe.
    Retorna None si el usuario ingresa 0 para volver.
    """
    while True:
        dni = input("\nIngrese el DNI del cliente (0: volver): ")

        if not dni.isdigit():
            print("El DNI debe ser un número, intente de nuevo...")
            continue
        if int(dni) == 0:
            return None

        for cliente in clientes:
            if cliente["dni"] == dni:
                return cliente["id"]

        print("No se encontró un cliente con ese DNI, intente de nuevo...")


# ─────────────────────────────────────────────
#  Planta
# ─────────────────────────────────────────────


def _calcular_stock_disponible(planta, items):
    """
    Calcula el stock real disponible de una planta,
    descontando lo que ya fue agregado en items de la venta actual.
    """
    stock = planta["stock"]
    for item in items:
        if item["id_planta"] == planta["id"]:
            stock -= item["cantidad"]
    return stock


def pedir_planta(plantas, items):
    """
    Solicita el ID de una planta y la retorna si existe y tiene stock.
    Retorna None si el usuario ingresa 0 para terminar.
    """
    while True:
        planta_id = input("\nIngrese el ID de la planta (0: terminar): ")

        if not planta_id.isdigit():
            print("El ID de la planta debe ser un número, intente de nuevo...")
            continue
        if int(planta_id) == 0:
            return None

        for planta in plantas:
            if planta["id"] == int(planta_id):
                if _calcular_stock_disponible(planta, items) == 0:
                    print("La planta no tiene stock disponible, ingrese otra...")
                    break
                return planta

        else:
            print("No se encontró una planta con ese ID, intente de nuevo...")


def pedir_cantidad(planta, items):
    """
    Solicita una cantidad válida para la planta dada.
    Retorna None si el usuario ingresa 0 para volver.
    """
    while True:
        cantidad = input("\nIngrese la cantidad (0: volver): ")

        if not cantidad.isdigit():
            print("La cantidad debe ser un número, intente de nuevo...")
            continue
        if int(cantidad) == 0:
            return None

        cantidad = int(cantidad)
        stock_disponible = _calcular_stock_disponible(planta, items)

        if cantidad <= stock_disponible:
            return cantidad

        print(
            f"La cantidad supera el stock disponible ({stock_disponible}), intente de nuevo..."
        )


# ─────────────────────────────────────────────
#  Forma de pago
# ─────────────────────────────────────────────


def pedir_forma_pago():
    """
    Solicita una forma de pago válida.
    Retorna None si el usuario ingresa 0 para salir.
    """
    while True:
        forma = input(f"\nForma de pago ({', '.join(FORMAS_PAGO)}, 0: salir): ")

        if forma.isdigit() and int(forma) == 0:
            return None
        if forma.lower() in FORMAS_PAGO:
            return forma.lower()

        print(f"Forma de pago inválida, las opciones son: {', '.join(FORMAS_PAGO)}...")


# ─────────────────────────────────────────────
#  Fecha
# ─────────────────────────────────────────────


def pedir_fecha():
    """
    Solicita una fecha en cualquier formato soportado.
    Retorna un objeto date o None si el usuario ingresa 0 para volver.
    """
    while True:
        entrada = input("\nIngrese la fecha (0: volver): ")

        if entrada.isdigit() and int(entrada) == 0:
            return None

        fecha = parsear_fecha(entrada)
        if fecha:
            return fecha

        print("Formato de fecha no reconocido, intente con dd/mm/yyyy o yyyy-mm-dd...")
