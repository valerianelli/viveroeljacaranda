from stock import menu_stock
from clientes import menu_clientes
from proveedores import menu_proveedores
from ventas import menu_ventas
from encargos import menu_encargos
from archivos import cargar_datos, guardar_datos

plantas = cargar_datos("plantas")
clientes = cargar_datos("clientes")
ventas = cargar_datos("ventas")
proveedores = cargar_datos("proveedores")
encargos = cargar_datos("encargos")


def mostrar_opciones():
    print("═══════════════════════════════════════════════════")
    print("       🌱 VIVERO EL JACARANDÁ — Sistema v1.0      ")
    print("═══════════════════════════════════════════════════")
    print("\n1. Stock de plantas")
    print("2. Clientes")
    print("3. Ventas")
    print("4. Proveedores")
    print("5. Encargos especiales")
    print("0. Salir\n")


def menu_principal():
    while True:
        mostrar_opciones()
        opcion = input("¿Que queres hacer? ")
        match opcion:
            case "1":
                menu_stock(plantas)
            case "2":
                menu_clientes(clientes)
            case "3":
                menu_ventas(ventas, clientes, plantas)
            case "4":
                menu_proveedores(proveedores)
            case "5":
                menu_encargos(encargos, clientes, proveedores)
            case "0":
                guardar_datos(plantas, "plantas")
                guardar_datos(clientes, "clientes")
                guardar_datos(ventas, "ventas")
                guardar_datos(proveedores, "proveedores")
                guardar_datos(encargos, "encargos")
                break
            case _:
                print("Opción inválida, intente de nuevo...\n")


menu_principal()
