from .constantes import SEPARADOR


def imprimir_items(items, plantas):
    """Imprime los items de una venta con nombre de planta, cantidad y precio."""
    for j, item in enumerate(items):
        planta = next((p for p in plantas if p["id"] == item["id_planta"]), None)
        nombre = planta["nombre_comun"] if planta else "Desconocida"

        print(f"    Planta ID: {item['id_planta']}")
        print(f"    Nombre común: {nombre}")
        print(f"    Cantidad: {item['cantidad']}")
        print(f"    Precio unitario: {item['precio_unit']:.2f}")

        if j != len(items) - 1:
            print()


def imprimir_venta(venta, plantas):
    """Imprime todos los datos de una venta individual."""
    print(f"Venta ID:      {venta['id']}")
    print(f"Cliente ID:    {venta['id_cliente']}")
    print(f"Fecha:         {venta['fecha']}")
    print(f"Total:         {venta['total']:.2f}")
    print(f"Forma de pago: {venta['forma_pago']}")
    print("Plantas vendidas:")
    imprimir_items(venta["items"], plantas)


def mostrar_ventas(ventas, plantas, id_cliente=None, fecha=None):
    """
    Muestra ventas filtradas por id_cliente o fecha.
    Si no se pasa ningún filtro, muestra todas.
    Retorna True si encontró resultados, False si no.
    """
    if id_cliente:
        ventas_a_mostrar = [v for v in ventas if v["id_cliente"] == id_cliente]
        mensaje_vacio = "No se encontraron ventas para ese cliente, intente de nuevo..."
    elif fecha:
        ventas_a_mostrar = [v for v in ventas if v["fecha"] == fecha]
        mensaje_vacio = "No se encontraron ventas en esa fecha, intente de nuevo..."
    else:
        ventas_a_mostrar = ventas
        mensaje_vacio = "Aún no hay ventas registradas."

    if not ventas_a_mostrar:
        print(mensaje_vacio)
        return False

    print()
    print(SEPARADOR)
    for i, venta in enumerate(ventas_a_mostrar):
        imprimir_venta(venta, plantas)
        if i != len(ventas_a_mostrar) - 1:
            print(SEPARADOR)
    print(SEPARADOR)

    return True
