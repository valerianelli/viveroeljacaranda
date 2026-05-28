from .proveedores import (
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

        opcion = input("Seleccione una opción: ").strip()

        match opcion:

            case "1":
                registrar_proveedor(proveedores_sistema)

            case "2":
                listar_proveedores(proveedores_sistema)

            case "3":
                buscar_proveedor(proveedores_sistema)

            case "4":
                actualizar_proveedor(proveedores_sistema)

            case "5":
                eliminar_proveedor(proveedores_sistema)

            case "0":
                print("Saliendo del menú proveedores.")

            case _:
                print("Opción inválida.")


menu_proveedores()
