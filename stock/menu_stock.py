# Modulo stock plantas

from.stock import (
   registrar_nueva_planta,
    obtener_todo_el_inventario,
    buscar_planta,
    actualizar_stock_planta,
    eliminar_planta
    ) 


# Menu principal 
def menu_stock(plantas):
    opcion = ""
    while opcion != "6":
        print("\n===== MENÚ STOCK DE PLANTAS =====")
        print("1. Cargar planta")
        print("2. Listar plantas")
        print("3. Buscar planta")
        print("4. Actualizar stock planta")
        print("5. Eliminar planta")
        print("6. Volver al menu principal")

        opcion = input("Seleccione una opción: ")

        match opcion:
            
            case "1":
                registrar_nueva_planta(plantas)
            case "2": 
                obtener_todo_el_inventario(plantas)
            case "3": 
                buscar_planta(plantas)
            case "4": 
                actualizar_stock_planta(plantas)
            case "5": 
                eliminar_planta(plantas)
            case "6": 
                print("Volviendo al menú principal...")
            case _: 
                print("Opción inválida. Por favor, Intente nuevamente.")

