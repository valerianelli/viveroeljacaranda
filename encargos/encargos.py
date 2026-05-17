from datetime import date

def generar_proximo_id(lista_encargos):
    """Genera un ID autoincremental único (pág. 6)"""
    if len(lista_encargos) == 0:
        return 1
    
    id_maximo = 0
    for e in lista_encargos:
        if e["id"] > id_maximo:
            id_maximo = e["id"]
    return id_maximo + 1

def registrar_encargo(lista_encargos, id_cliente, id_proveedor, descripcion, cantidad, sena):
    """
    Registra un encargo en la lista recibida.
    Valida tipos de datos sin usar isinstance.
    """
    # Validaciones técnicas (pág. 6)
    if type(id_cliente) != int or type(id_proveedor) != int:
        return "Error: Los IDs deben ser números enteros."
    if type(cantidad) != int or cantidad <= 0:
        return "Error: La cantidad debe ser un entero positivo."
    if type(sena) != float and type(sena) != int:
        return "Error: La seña debe ser un valor numérico."

    nuevo = {
        "id": generar_proximo_id(lista_encargos),
        "id_cliente": id_cliente,
        "id_proveedor": id_proveedor,
        "descripcion": str(descripcion),
        "cantidad": cantidad,
        "fecha_pedido": date.today(),
        "fecha_estimada_llegada": date.today(), # Se asume fecha actual por defecto
        "estado": "pedido",
        "sena": float(sena)
    }
    
    lista_encargos.append(nuevo)
    return nuevo

def cambiar_estado(lista_encargos, id_buscado, nuevo_estado):
    """Modifica el estado de un encargo existente"""
    for e in lista_encargos:
        if e["id"] == id_buscado:
            e["estado"] = nuevo_estado
            return True
    return False

def eliminar_encargo_fisico(lista_encargos, id_buscado):
    """Elimina el registro de la lista"""
    for i in range(len(lista_encargos)):
        if lista_encargos[i]["id"] == id_buscado:
            lista_encargos.pop(i)
            return True
    return False
