from .clientes import (
    cargar_cliente,
    listar_clientes,
    buscar_cliente,
    modificar_cliente,
    eliminar_cliente
)


def menu_clientes(clientes):
    opcion = ""

    while opcion != "6":
        print("\n===== MENÚ CLIENTES =====")
        print("1. Cargar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Modificar cliente")
        print("5. Eliminar cliente")
        print("6. Volver al menú principal")

        opcion = input("Ingrese una opción: ")

        match opcion:
            case "1":
                cargar_cliente(clientes)
            case "2":
                listar_clientes(clientes)
            case "3":
                buscar_cliente(clientes)
            case "4":
                modificar_cliente(clientes)
            case "5":
                eliminar_cliente(clientes)
            case "6":
                print("Volviendo al menú principal...")
            case _:
                print("Opción incorrecta. Intente nuevamente.")
