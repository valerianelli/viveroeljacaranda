from datetime import date

def generar_proximo_id(lista_encargos):
    if not lista_encargos:
        return 1
    return maximo_id(lista_encargos) + 1

def maximo_id(lista_encargos):
    id_maximo = lista_encargos[0]["id"]
    tail = lista_encargos[1:]
    for encargo in tail:
        encargo_id = encargo["id"]
        if encargo_id > id_maximo:
            id_maximo = encargo_id
    return id_maximo

def registrar_encargo(lista_encargos, id_cliente, id_proveedor, descripcion, cantidad, sena, fecha_estimada):
    nuevo = {
        "id": generar_proximo_id(lista_encargos),
        "id_cliente": id_cliente,
        "id_proveedor": id_proveedor,
        "descripcion": descripcion,
        "cantidad": cantidad,
        "fecha_pedido": str(date.today()),
        "fecha_estimada_llegada": fecha_estimada,
        "estado": "pedido",
        "sena": sena
    }
    lista_encargos.append(nuevo)
    return nuevo


def cambiar_estado(lista_encargos, id_buscado, nuevo_estado):
    for encargo in lista_encargos:
        if encargo["id"] == id_buscado:
            encargo["estado"] = nuevo_estado
            return True
    return False


def eliminar_encargo(lista_encargos, id_buscado):
    for indice, encargo in enumerate(lista_encargos):
        if encargo["id"] == id_buscado:
            lista_encargos.pop(indice)
            return True
    return False


def buscar_por_cliente(lista_encargos, id_cliente):
    resultado = []
    for encargo in lista_encargos:
        if encargo["id_cliente"] == id_cliente:
            resultado.append(encargo)
    return resultado


def buscar_por_proveedor(lista_encargos, id_proveedor):
    resultado = []
    for encargo in lista_encargos:
        if encargo["id_proveedor"] == id_proveedor:
            resultado.append(encargo)
    return resultado


def buscar_por_fecha(lista_encargos, fecha):
    resultado = []
    for encargo in lista_encargos:
        if (encargo["fecha_pedido"] == fecha or 
            encargo["fecha_estimada_llegada"] == fecha):
            resultado.append(encargo)
    return resultado

def obtener_cliente_por_id(id_cliente, lista_clientes):
    for cliente in lista_clientes:
        if cliente["id"] == id_cliente:
            return cliente
    return None


def obtener_proveedor_por_id(id_proveedor, lista_proveedores):
    for proveedor in lista_proveedores:
        if proveedor["id"] == id_proveedor:
            return proveedor
    return None
