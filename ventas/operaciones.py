from datetime import date
from copy import deepcopy
import re

from .constantes import (
    FORMAS_PAGO,
    parsear_fecha,
    buscar_por_id,
    pedir_confirmacion,
    imprimir_exito,
)
from .inputs import pedir_cliente, pedir_planta, pedir_cantidad, pedir_forma_pago
from .visualizacion import mostrar_ventas, imprimir_items

# ─────────────────────────────────────────────
#  Registrar
# ─────────────────────────────────────────────


def registrar_venta(ventas, clientes, plantas):
    """Guía al usuario para registrar una nueva venta completa."""
    id_cliente = pedir_cliente(clientes)
    if not id_cliente:
        return

    items = _agregar_items(plantas)
    if not items:
        return

    forma_pago = pedir_forma_pago()
    if not forma_pago:
        return

    _descontar_stock(items, plantas)
    total = _calcular_total(items)
    _guardar_venta(ventas, id_cliente, items, total, forma_pago)

    imprimir_exito("Venta cargada correctamente!")


def _agregar_items(plantas):
    """Loop que acumula items hasta que el usuario termine."""
    items = []
    while True:
        planta = pedir_planta(plantas, items)
        if not planta:
            break

        cantidad = pedir_cantidad(planta, items)
        if not cantidad:
            break

        items.append(
            {
                "id_planta": planta["id"],
                "cantidad": cantidad,
                "precio_unit": planta["precio"],
            }
        )

    return items


def _descontar_stock(items, plantas):
    """Resta del stock de cada planta la cantidad vendida."""
    for item in items:
        planta = buscar_por_id(plantas, item["id_planta"])
        if planta:
            planta["stock"] -= item["cantidad"]


def _calcular_total(items):
    """Suma cantidad * precio_unit de todos los items."""
    return sum(item["cantidad"] * item["precio_unit"] for item in items)


def _guardar_venta(ventas, id_cliente, items, total, forma_pago):
    """Crea el diccionario de venta y lo agrega a la lista."""
    nueva_id = max((v["id"] for v in ventas), default=0) + 1
    ventas.append(
        {
            "id": nueva_id,
            "id_cliente": id_cliente,
            "fecha": date.today(),
            "items": items,
            "total": total,
            "forma_pago": forma_pago,
        }
    )


# ─────────────────────────────────────────────
#  Buscar
# ─────────────────────────────────────────────


def buscar_venta(ventas, clientes, plantas):
    """Permite buscar ventas por DNI del cliente o por fecha."""
    while True:
        entrada = input(
            "\nIngrese el DNI del cliente o la fecha de la venta (0: volver): "
        )

        if entrada.isdigit():
            if int(entrada) == 0:
                return
            if _buscar_por_dni(ventas, clientes, plantas, entrada):
                break
            continue

        if _buscar_por_fecha(ventas, plantas, entrada):
            break


def _buscar_por_dni(ventas, clientes, plantas, dni):
    """Busca el cliente por DNI y muestra sus ventas. Retorna True si encontró."""
    cliente = next((c for c in clientes if c["dni"] == dni), None)
    if not cliente:
        print("No se encontró un cliente con ese DNI, intente de nuevo...")
        return False
    return mostrar_ventas(ventas, plantas, id_cliente=cliente["id"])


def _buscar_por_fecha(ventas, plantas, entrada):
    """Parsea la fecha ingresada y muestra las ventas de ese día. Retorna True si encontró."""
    partes = re.split(r"[/\-_|.,:;#]|\s+del?\s+|\s+", entrada)
    if len(partes) != 3:
        print("Formato de fecha no reconocido, intente con dd/mm/yyyy o yyyy-mm-dd...")
        return False

    fecha = parsear_fecha(entrada)
    if not fecha:
        return False

    return mostrar_ventas(ventas, plantas, fecha=fecha)


# ─────────────────────────────────────────────
#  Modificar
# ─────────────────────────────────────────────


def modificar_venta(ventas, clientes, plantas):
    """Permite modificar los datos de una venta existente."""
    while True:
        id_venta = input("\nIngrese ID de la venta (0: volver): ")

        if not id_venta.isdigit():
            print("El ID debe ser un número, intente de nuevo...")
            continue
        if int(id_venta) == 0:
            break

        venta = buscar_por_id(ventas, int(id_venta))
        if not venta:
            print("No se encontró una venta con ese ID, intente de nuevo...")
            continue

        datos_nuevos = _pedir_datos_nuevos(venta, clientes, plantas)
        if not datos_nuevos:
            break

        if pedir_confirmacion("¿Confirmar modificación? (si/no): "):
            _aplicar_modificacion(venta, datos_nuevos, plantas)
            imprimir_exito("Venta actualizada correctamente!")

        break


def _pedir_datos_nuevos(venta, clientes, plantas):
    """
    Recorre cada campo de la venta y ofrece al usuario modificarlo.
    Retorna un dict con los nuevos valores, o None si el usuario canceló.
    """
    datos_nuevos = {}

    for clave, valor in venta.items():
        if clave == "id":
            continue

        match clave:
            case "id_cliente":
                resultado = _modificar_id_cliente(datos_nuevos, valor, clientes)
            case "fecha":
                resultado = _modificar_fecha(datos_nuevos, valor)
            case "items":
                resultado = _modificar_items(datos_nuevos, valor, plantas)
            case "total":
                _recalcular_total(datos_nuevos, valor)
                resultado = True
            case "forma_pago":
                resultado = _modificar_forma_pago(datos_nuevos, valor)
                resultado = True

        if not resultado:
            return None

    return datos_nuevos


def _modificar_id_cliente(datos_nuevos, valor_actual, clientes):
    while True:
        print(f"\nID del cliente (actual): {valor_actual}")
        entrada = input("Ingrese ID de cliente nuevo (0: volver, -1: siguiente): ")

        if entrada == "-1":
            return True
        if not entrada.isdigit():
            print("El ID debe ser un número, intente de nuevo...")
            continue
        if int(entrada) == 0:
            return False
        if int(entrada) == valor_actual:
            print("El ID ingresado es igual al actual, ingrese uno diferente...")
            continue

        if buscar_por_id(clientes, int(entrada)):
            datos_nuevos["id_cliente"] = int(entrada)
            return True

        print("No se encontró un cliente con ese ID, intente de nuevo...")


def _modificar_fecha(datos_nuevos, valor_actual):
    while True:
        print(f"\nFecha (actual): {valor_actual}")
        entrada = input("Ingrese la nueva fecha (0: volver, -1: siguiente): ")

        if entrada == "-1":
            return True
        if entrada.isdigit() and int(entrada) == 0:
            return False

        partes = re.split(r"[/\-_|.,:;#]|\s+del?\s+|\s+", entrada)
        if len(partes) != 3:
            print(
                "Formato de fecha no reconocido, intente con dd/mm/yyyy o yyyy-mm-dd..."
            )
            continue

        fecha = parsear_fecha(entrada)
        if fecha:
            datos_nuevos["fecha"] = fecha
            return True


def _modificar_items(datos_nuevos, items_actuales, plantas):
    datos_nuevos["items"] = deepcopy(items_actuales)

    while True:
        print("\nPlantas vendidas (actual):")
        imprimir_items(datos_nuevos["items"], plantas)

        entrada = input("\nIngrese ID de la planta (0: volver, -1: siguiente): ")

        if entrada == "-1":
            return True
        if not entrada.isdigit():
            print("El ID debe ser un número, intente de nuevo...")
            continue
        if int(entrada) == 0:
            return False

        item = next(
            (i for i in datos_nuevos["items"] if i["id_planta"] == int(entrada)), None
        )
        if not item:
            print(
                "No se encontró una planta con ese ID en la venta, intente de nuevo..."
            )
            continue

        planta = buscar_por_id(plantas, int(entrada))
        if not planta:
            print("La planta ya no existe en el stock, ingrese otra...")
            continue

        _modificar_cantidad_item(item, planta, datos_nuevos["items"])


def _modificar_cantidad_item(item, planta, items):
    while True:
        entrada = input(
            "\nIngrese la nueva cantidad (0: volver, -1: siguiente, vacío: eliminar): "
        )

        if entrada == "":
            items.remove(item)
            return
        if entrada == "-1":
            return
        if entrada.isdigit() and int(entrada) == 0:
            return
        if entrada.isdigit() and int(entrada) > 0:
            if int(entrada) <= planta["stock"]:
                item["cantidad"] = int(entrada)
                return
            print(
                f"La cantidad supera el stock disponible ({planta['stock']}), intente de nuevo..."
            )
            continue

        print("La cantidad debe ser un número positivo, intente de nuevo...")


def _recalcular_total(datos_nuevos, valor_actual):
    print(f"\nTotal (actual): {valor_actual:.2f}")
    total = sum(
        item["cantidad"] * item["precio_unit"] for item in datos_nuevos["items"]
    )
    datos_nuevos["total"] = total
    print(f"Total nuevo: {total:.2f}")


def _modificar_forma_pago(datos_nuevos, valor_actual):
    while True:
        print(f"\nForma de pago (actual): {valor_actual}")
        entrada = input(
            f"Ingrese la nueva forma de pago ({', '.join(FORMAS_PAGO)}, -1: siguiente): "
        ).lower()

        if entrada == "-1":
            return True
        if entrada == valor_actual:
            print(
                "La forma de pago ingresada es igual a la actual, ingrese una diferente..."
            )
            continue
        if entrada in FORMAS_PAGO:
            datos_nuevos["forma_pago"] = entrada
            return True

        print(f"Forma de pago inválida, las opciones son: {', '.join(FORMAS_PAGO)}...")


def _aplicar_modificacion(venta, datos_nuevos, plantas):
    """
    Ajusta el stock según los cambios en los items y aplica los nuevos datos a la venta.
    """
    _ajustar_stock_por_modificacion(venta["items"], datos_nuevos["items"], plantas)
    for clave, valor in datos_nuevos.items():
        venta[clave] = valor


def _ajustar_stock_por_modificacion(items_viejos, items_nuevos, plantas):
    """
    Compara items viejos y nuevos para ajustar el stock:
    - Si se redujo cantidad → devuelve la diferencia al stock
    - Si se aumentó cantidad → descuenta la diferencia del stock
    - Si se eliminó un item → devuelve toda la cantidad al stock
    - Si se agregó un item nuevo → descuenta del stock
    """
    for item_viejo in items_viejos:
        item_nuevo = next(
            (i for i in items_nuevos if i["id_planta"] == item_viejo["id_planta"]), None
        )
        planta = buscar_por_id(plantas, item_viejo["id_planta"])

        if not planta:
            continue

        if not item_nuevo:
            # El item fue eliminado: devolver stock completo
            planta["stock"] += item_viejo["cantidad"]
        elif item_viejo["cantidad"] != item_nuevo["cantidad"]:
            # La cantidad cambió: ajustar la diferencia
            diferencia = item_viejo["cantidad"] - item_nuevo["cantidad"]
            planta["stock"] += diferencia  # positivo = devuelve, negativo = descuenta

    for item_nuevo in items_nuevos:
        es_nuevo = not any(
            i["id_planta"] == item_nuevo["id_planta"] for i in items_viejos
        )
        if es_nuevo:
            planta = buscar_por_id(plantas, item_nuevo["id_planta"])
            if planta:
                planta["stock"] -= item_nuevo["cantidad"]


# ─────────────────────────────────────────────
#  Eliminar
# ─────────────────────────────────────────────


def eliminar_venta(ventas, plantas):
    """Permite eliminar una venta existente y restaura el stock correspondiente."""
    while True:
        id_venta = input("\nIngrese ID de la venta (0: volver): ")

        if not id_venta.isdigit():
            print("El ID debe ser un número, intente de nuevo...")
            continue
        if int(id_venta) == 0:
            break

        venta = buscar_por_id(ventas, int(id_venta))
        if not venta:
            print("No se encontró una venta con ese ID, intente de nuevo...")
            continue

        if not pedir_confirmacion("¿Confirmar borrado? (si/no): "):
            break

        _restaurar_stock(venta["items"], plantas)
        ventas.remove(venta)
        imprimir_exito("Venta borrada correctamente!")
        break


def _restaurar_stock(items, plantas):
    """Devuelve al stock de cada planta la cantidad que estaba en la venta eliminada."""
    for item in items:
        planta = buscar_por_id(plantas, item["id_planta"])
        if planta:
            planta["stock"] += item["cantidad"]
