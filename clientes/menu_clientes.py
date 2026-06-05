from .clientes import (
    cargar_cliente,
    listar_clientes,
    buscar_cliente,
    modificar_cliente,
    eliminar_cliente
)

def menu_clientes(clientes, ventas, plantas, encargos):
    seguir = True

    while seguir:
        print("\n========== MENÚ CLIENTES ==========")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Modificar cliente")
        print("5. Eliminar cliente")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                cargar_cliente(clientes)
            case "2":
                listar_clientes(clientes)
            case "3":
                buscar_cliente(clientes, ventas, plantas, encargos)
            case "4":
                modificar_cliente(clientes)
            case "5":
                eliminar_cliente(clientes)
            case "0":
                seguir = False
            case _:
                print("Opción incorrecta. Intente nuevamente.")
