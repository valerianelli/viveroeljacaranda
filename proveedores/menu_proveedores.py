from proveedores import (
    registrar_proveedor,
    listar_proveedores,
    buscar_proveedor,
    actualizar_proveedor,
    eliminar_proveedor
)


def menu_proveedores():

    opcion = ""

    while opcion != "0":

        print("\n===== MENÚ PROVEEDORES =====")
        print("1. Registrar proveedor")
        print("2. Listar proveedores")
        print("3. Buscar proveedor")
        print("4. Actualizar proveedor")
        print("5. Eliminar proveedor")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        match opcion:

            case "1":
                registrar_proveedor()

            case "2":
                listar_proveedores()

            case "3":
                buscar_proveedor()

            case "4":
                actualizar_proveedor()

            case "5":
                eliminar_proveedor()

            case "0":
                print("Saliendo del sistema...")

            case _:
                print("Opción inválida.")


menu_proveedores()