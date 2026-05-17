from encargos.encargos import registrar_encargo, cambiar_estado, eliminar_encargo_fisico

def mostrar_encargo(e):
    """Imprime un encargo de forma amigable"""
    print(f"[{e['id']}] Cliente ID: {e['id_cliente']} | {e['descripcion']} | Estado: {e['estado'].upper()}")

def menu_encargos(lista_encargos, lista_clientes, lista_proveedores):
    """Controlador del área de encargos (pág. 5)"""
    while True:
        print("\n═══════════════════════════════════════════════════")
        print("                ENCARGOS ESPECIALES                ")
        print("═══════════════════════════════════════════════════")
        print("1. Cargar un nuevo encargo")
        print("2. Ver listado de encargos activos")
        print("3. Buscar encargos por cliente")
        print("4. Actualizar estado (pedido, llegó, entregado)")
        print("5. Dar de baja un encargo")
        print("9. Volver a la pantalla principal")
        
        opcion = input("\n¿Qué querés hacer? ")

        if opcion == "1":
            try:
                id_c = int(input("ID del Cliente: "))
                id_p = int(input("ID del Proveedor: "))
                desc = input("Descripción (ej: Limonero 4 patas): ")
                cant = int(input("Cantidad: "))
                sena = float(input("Seña recibida: "))
                
                resultado = registrar_encargo(lista_encargos, id_c, id_p, desc, cant, sena)
                if type(resultado) == str:
                    print(resultado)
                else:
                    print("✓ Encargo guardado exitosamente.")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")

        elif opcion == "2":
            print("\n--- ENCARGOS ACTIVOS ---")
            hay = False
            for e in lista_encargos:
                if e["estado"] not in ["entregado", "cancelado"]:
                    mostrar_encargo(e)
                    hay = True
            if not hay: print("No hay encargos activos.")

        elif opcion == "3":
            try:
                id_c = int(input("Ingrese ID del cliente: "))
                print(f"\nEncargos del cliente {id_c}:")
                for e in lista_encargos:
                    if e["id_cliente"] == id_c:
                        mostrar_encargo(e)
            except ValueError:
                print("ID inválido.")

        elif opcion == "4":
            try:
                id_e = int(input("ID del encargo a modificar: "))
                nuevo = input("Nuevo estado (pedido/llegó/entregado/cancelado): ")
                if cambiar_estado(lista_encargos, id_e, nuevo.lower()):
                    print("✓ Estado actualizado.")
                else:
                    print("X No se encontró el encargo.")
            except ValueError:
                print("Dato inválido.")

        elif opcion == "5":
            try:
                id_e = int(input("ID del encargo a borrar: "))
                # Confirmación obligatoria (pág. 5)
                conf = input(f"¿Seguro que desea eliminar el encargo {id_e}? (s/n): ")
                if conf.lower() == 's':
                    if eliminar_encargo_fisico(lista_encargos, id_e):
                        print("✓ Registro eliminado.")
                    else:
                        print("X ID no encontrado.")
            except ValueError:
                print("Dato inválido.")

        elif opcion == "9":
            break
        else:
            print("Opción inválida.")
