from encargos.encargos import (
    registrar_encargo, cambiar_estado, eliminar_encargo,
    buscar_por_cliente, buscar_por_proveedor, buscar_por_fecha,
    obtener_cliente_por_id, obtener_proveedor_por_id
)
from ventas.constantes import parsear_fecha


def mostrar_encargo(encargo):
    print(f"  [{encargo['id']}] {encargo['descripcion']} x{encargo['cantidad']}")
    print(f"       Cliente ID: {encargo['id_cliente']} | Proveedor ID: {encargo['id_proveedor']}")
    print(f"       Pedido: {encargo['fecha_pedido']} | Llegada estimada: {encargo['fecha_estimada_llegada']}")
    print(f"       Estado: {encargo['estado'].upper()} | Seña: ${encargo['sena']:.2f}")


def _existe_cliente(cliente_id, lista_clientes):
    for cliente in lista_clientes:
        if cliente["id"] == cliente_id:
            return True
    return False


def _existe_proveedor(proveedor_id, lista_proveedores):
    for proveedor in lista_proveedores:
        if proveedor["id"] == proveedor_id:
            return True
    return False


def _pedir_id_cliente(lista_clientes):
    while True:
        try:
            id_cliente_ingresado = int(input("ID del Cliente: "))
            if _existe_cliente(id_cliente_ingresado, lista_clientes):
                return id_cliente_ingresado
            print("\nEse ID de cliente no existe. Revisá y probá de nuevo.")
        except ValueError:
            print("\nEso no es un número válido. Ingresá solo números.")


def _pedir_id_proveedor(lista_proveedores):
    while True:
        try:
            id_proveedor_ingresado = int(input("ID del Proveedor: "))
            if _existe_proveedor(id_proveedor_ingresado, lista_proveedores):
                return id_proveedor_ingresado
            print("Ese ID de proveedor no existe. Revisá y probá de nuevo.")
        except ValueError:
            print("Eso no es un número válido. Ingresá solo números.")


def _pedir_descripcion():
    while True:
        descripcion = input("Descripción (ej: Limonero de 4 patas, 1.5 metros): ").strip()
        if descripcion:
            return descripcion
        print("La descripción no puede estar vacía. Contame qué planta es.")


def _pedir_cantidad():
    while True:
        try:
            cant = int(input("Cantidad: "))
            if cant > 0:
                return cant
            print("La cantidad tiene que ser mayor a cero.")
        except ValueError:
            print("Eso no es un número entero. Ingresá la cantidad.")


def _pedir_sena():
    while True:
        try:
            sena = float(input("Seña recibida ($): "))
            if sena >= 0:
                return sena
            print(f"\nLa seña no puede ser negativa.")
        except ValueError:
            print(f"\nEso no es un número válido. Ingresá el monto.")


def _pedir_fecha():
    while True:
        fecha_str = input("Fecha (ej: 15/06/2026 o 2026-06-15): ").strip()
        if not fecha_str:
            print("\nLa fecha no puede estar vacía.")
            continue
        fecha = parsear_fecha(fecha_str)
        if fecha:
            return fecha
        print(f"\nNo se entendió la fecha. Intentá de nuevo.")


def _pedir_id_encargo(lista_encargos, mensaje="ID del encargo"):
    while True:
        try:
            id_encargo_ingresado = int(input(f"{mensaje}: "))
            for encargo in lista_encargos:
                if encargo["id"] == id_encargo_ingresado:
                    return id_encargo_ingresado
            print(f"\nNo existe un encargo con ese ID. Verificá.")
        except ValueError:
            print(f"\nEso no es un número válido.")


def _pedir_estado():
    estados = {"1": "pedido", "2": "llegó", "3": "entregado", "4": "cancelado"}
    print("Estados disponibles:")
    print("  1. Pedido")
    print("  2. Llegó")
    print("  3. Entregado")
    print("  4. Cancelado")
    while True:
        opcion = input("Elegí el nuevo estado (1-4): ").strip()
        if opcion in estados:
            return estados[opcion]
        print("\nOpción inválida. Elegí 1, 2, 3 o 4.")


def _mostrar_datos_cliente(id_cliente, lista_clientes):
    cliente = obtener_cliente_por_id(id_cliente, lista_clientes)
    if cliente:
        print(f"\n  ¡Llamalo ya! Datos del cliente:")
        print(f"    Nombre: {cliente['nombre_completo']}")
        print(f"    Teléfono: {cliente['telefono']}")
        if cliente["email"]:
            print(f"    Email: {cliente['email']}")


def dame_activos(lista_encargos):
    resultados = []
    for encargo in lista_encargos:
        if encargo["estado"] not in ("entregado", "cancelado"):
            resultados.append(encargo)
    return resultados

def menu_encargos(lista_encargos, lista_clientes, lista_proveedores):
    while True:
        print("\n═══════════════════════════════════════════════════")
        print("                ENCARGOS ESPECIALES                ")
        print("═══════════════════════════════════════════════════")
        print("1. Cargar un nuevo encargo")
        print("2. Ver listado de encargos activos")
        print("3. Buscar encargos")
        print("4. Actualizar estado")
        print("5. Cancelar un encargo")
        print("9. Volver a la pantalla principal")

        opcion = input("\n¿Qué querés hacer? ")

        if opcion == "1":
            print("\n--- NUEVO ENCARGO ---")
            if not lista_clientes:
                print("No hay clientes registrados. Primero cargá uno.")
                continue
            if not lista_proveedores:
                print("No hay proveedores registrados. Primero cargá uno.")
                continue

            id_cliente_ingresado = _pedir_id_cliente(lista_clientes)
            id_proveedor_ingresado = _pedir_id_proveedor(lista_proveedores)
            descripcion = _pedir_descripcion()
            cantidad = _pedir_cantidad()
            # Seña
            sena = _pedir_sena()
            print("Fecha estimada de llegada:")
            fecha_estimada_llegada = _pedir_fecha()

            resultado = registrar_encargo(lista_encargos,
                id_cliente_ingresado,
                id_proveedor_ingresado,
                descripcion,
                cantidad,
                sena,
                fecha_estimada_llegada)
            print(f"✓ Encargo #{resultado['id']} guardado exitosamente.")

        elif opcion == "2":
            print("\n--- ENCARGOS ACTIVOS ---")
            activos = dame_activos(lista_encargos)
            if not activos:
                print("\nNo hay encargos activos.")
            else:
                for encargo in activos:
                    print()
                    mostrar_encargo(encargo)

        elif opcion == "3":
            print("\n--- BUSCAR ENCARGOS ---")
            print("1. Por cliente")
            print("2. Por proveedor")
            print("3. Por fecha")
            opcion_submenu = input("Elegí cómo buscar: ")

            if opcion_submenu == "1":
                if not lista_clientes:
                    print("No hay clientes registrados.")
                    continue
                id_cliente = _pedir_id_cliente(lista_clientes)
                resultados = buscar_por_cliente(lista_encargos, id_cliente)
                if not resultados:
                    print("\nNo se encontraron encargos para ese cliente.")
                else:
                    for encargo in resultados:
                        print()
                        mostrar_encargo(encargo)

            elif opcion_submenu == "2":
                if not lista_proveedores:
                    print("No hay proveedores registrados.")
                    continue
                id_proveedor = _pedir_id_proveedor(lista_proveedores)
                resultados = buscar_por_proveedor(lista_encargos, id_proveedor)
                if not resultados:
                    print("\nNo se encontraron encargos para ese proveedor.")
                else:
                    for encargo in resultados:
                        print()
                        mostrar_encargo(encargo)

            elif opcion_submenu == "3":
                print("Fecha a buscar (puede ser fecha de pedido o de llegada estimada):")
                fecha = _pedir_fecha()
                resultados = buscar_por_fecha(lista_encargos, fecha)
                if not resultados:
                    print("\nNo se encontraron encargos para esa fecha.")
                else:
                    for encargo in resultados:
                        print()
                        mostrar_encargo(encargo)

            else:
                print("Opción inválida. Volvé a intentar.")

        elif opcion == "4":
            print("\n--- ACTUALIZAR ESTADO ---")
            if not lista_encargos:
                print("\nNo hay encargos registrados.")
                continue

            id_encargo_ingresado = _pedir_id_encargo(lista_encargos)

            for encargo in lista_encargos:
                if encargo["id"] == id_encargo_ingresado:
                    print()
                    mostrar_encargo(encargo)
                    break

            nuevo_estado = _pedir_estado()

            if cambiar_estado(lista_encargos, id_encargo_ingresado, nuevo_estado):
                print(f"✓ Estado actualizado a '{nuevo_estado}'.")

                if nuevo_estado == "llegó":
                    for encargo in lista_encargos:
                        if encargo["id"] == id_encargo_ingresado:
                            _mostrar_datos_cliente(encargo["id_cliente"], lista_clientes)
                            break
            else:
                print("\n X No se encontró el encargo.")

        elif opcion == "5":
            print("\n--- CANCELAR ENCARGO ---")
            if not lista_encargos:
                print("\nNo hay encargos registrados.")
                continue

            id_encargo_ingresado = _pedir_id_encargo(lista_encargos)

            for encargo in lista_encargos:
                if encargo["id"] == id_encargo_ingresado:
                    print("\nEncargo a cancelar:")
                    mostrar_encargo(encargo)
                    break

            conf = input("\n¿Estás seguro de que querés cancelar este encargo? (s/n): ").lower()
            if conf == "s":
                if cambiar_estado(lista_encargos, id_encargo_ingresado, "cancelado"):
                    print("\n✓ Encargo cancelado.")
                else:
                    print("\nX No se encontró el encargo.")
            else:
                print("\nCancelación cancelada.")

        elif opcion == "9":
            break

        else:
            print("\nUps, esa opción no existe. Elegí otra, ¡con confianza!")
