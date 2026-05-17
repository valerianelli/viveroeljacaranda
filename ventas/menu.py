from .visualizacion import mostrar_ventas
from .operaciones import registrar_venta, buscar_venta, modificar_venta, eliminar_venta


def mostrar_menu():
    print("\n═══════════════════════════════════════════════════")
    print("                   💰 VENTAS                      ")
    print("═══════════════════════════════════════════════════\n")
    print("1. Registrar venta")
    print("2. Ver ventas")
    print("3. Buscar venta")
    print("4. Modificar venta")
    print("5. Eliminar venta")
    print("0. Volver al menú principal\n")


def menu_ventas(ventas, clientes, plantas):
    while True:
        mostrar_menu()
        opcion = input("¿Qué querés hacer? ")

        match opcion:
            case "1":
                registrar_venta(ventas, clientes, plantas)
            case "2":
                mostrar_ventas(ventas, plantas)
            case "3":
                buscar_venta(ventas, clientes, plantas)
            case "4":
                modificar_venta(ventas, clientes, plantas)
            case "5":
                eliminar_venta(ventas, plantas)
            case "0":
                break
            case _:
                print("Opción inválida, intente de nuevo...")
