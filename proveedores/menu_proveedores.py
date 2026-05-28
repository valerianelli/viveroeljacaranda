from proveedores import (
    registrar_proveedor,
    listar_proveedores,
    buscar_proveedor,
    actualizar_proveedor,
    eliminar_proveedor
)

# 1. Agregar el parámetro (lista_proveedores) aquí en la definición
def menu_proveedores(lista_proveedores): 
    
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
                # Pasar la lista a la función
                registrar_proveedor(lista_proveedores)
            case "2":
                listar_proveedores(lista_proveedores)
            case "3":
                buscar_proveedor(lista_proveedores)
            case "4":
                actualizar_proveedor(lista_proveedores)
            case "5":
                eliminar_proveedor(lista_proveedores)
            case "0":
                print("Saliendo del menú de proveedores...")
            case _:
                print("Opción inválida.")
