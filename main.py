from stock import menu_stock
from clientes import menu_clientes
from proveedores import menu_proveedores
from ventas import menu_ventas
from encargos.menu_encargos import menu_encargos

plantas = []
clientes = []
ventas = []
proveedores = []
encargos = []


def mostrar_opciones():
    print("═══════════════════════════════════════════════════")
    print("       🌱 VIVERO EL JACARANDÁ — Sistema v1.0      ")
    print("═══════════════════════════════════════════════════")
    print("")
    print("1. Stock de plantas")
    print("2. Clientes")
    print("3. Ventas")
    print("4. Proveedores")
    print("5. Encargos especiales")
    print("0. Salir")
    print("")


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
                break
            case _:
                print("Opción inválida, intente denuevo...\n")


menu_principal()
