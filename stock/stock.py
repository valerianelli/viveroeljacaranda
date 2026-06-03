# Modulo stock de plantas #estructura de datos

# 2-Funciones de logica y vistas combinadas 

def generar_proximo_id(plantas):
    """Revisa las plantas existentes y devuelve el ID más alto + 1"""
    if len(plantas) == 0:
        return 1
    
    id_maximo = 0
    for p in plantas:
        if p["id"] > id_maximo:
            id_maximo = p["id"]
    return id_maximo + 1

def buscar_planta_por_id(plantas, id):
    """Recorre la lista y devuelve la planta cuyo ID coincide, o None."""
    for planta in plantas:
        if planta["id"] == id:
            return planta
    return None

def buscar_plantas_por_texto(plantas, texto):
    """Devuelve una lista con todas las plantas que contienen el texto en nombre común o científico."""
    texto = texto.lower()
    resultados = []
    for planta in plantas:
        if texto in planta["nombre_comun"].lower() or texto in planta["nombre_cientifico"].lower():
            resultados.append(planta)
    return resultados

def planta_ya_existe(plantas, nombre_comun, nombre_cientifico):
    """
    Busca si ya existe una planta con el mismo nombre común Y científico.
    Devuelve la planta encontrada o None.
    """
    nombre_comun = nombre_comun.lower()
    nombre_cientifico = nombre_cientifico.lower()
    for planta in plantas:
        if planta["nombre_comun"].lower() == nombre_comun and planta["nombre_cientifico"].lower() == nombre_cientifico :
            return planta
    return None

def registrar_nueva_planta(plantas): 
    nombre_comun, nombre_cientifico, categoria, sector, stock, precio, cuidados = cargar_planta()
    planta_existente = planta_ya_existe(plantas, nombre_comun, nombre_cientifico)
    
    if planta_existente:
        print(f"\n  ADVERTENCIA: Ya existe una planta llamada '{nombre_comun}' / '{nombre_cientifico}'.(codigo identificador en el inventario: {planta_existente['id']})")
        print("Tiene estos datos:.\n ")
        mostrar_planta(planta_existente)
        decision = input("  ¿Desea cargarla como una planta nueva de todas formas? (s/n): ").strip().lower()
        if decision != "s":
            print("  Carga cancelada.")
            return

    # Usamos la nueva función para obtener el ID real basado en los datos guardados
    nuevo_id = generar_proximo_id(plantas)

    nueva_planta = {
        "id": nuevo_id,
        "nombre_comun": nombre_comun,
        "nombre_cientifico": nombre_cientifico,
        "categoria": categoria,
        "sector": sector,
        "stock": stock,
        "precio": precio,
        "cuidados": cuidados
    }
    
    plantas.append(nueva_planta)
    print(f"\n Planta '{nombre_comun}' cargada correctamente con el código identificador {nuevo_id}.")

def obtener_todo_el_inventario(plantas):
    if not plantas:
        print("\nEl inventario está vacío.")
        return
        
    print("\n===== OPCIONES DE LISTADO =====")
    print("1. Ver el listado completo")
    print("2. Filtrar por sector (Interior, Exterior, Invernadero, Huerta)")
    print("3. Filtrar por categoría (Árbol, Arbusto, Suculenta, Aromática, Frutal, Ornamental, Otro)")
    
    opcion = input("Seleccione una opción de listado: ")
    
    if opcion == "1":
        print("\n--- LISTADO COMPLETO DE PLANTAS ---")
        for planta in plantas: 
            mostrar_planta(planta)
            
    elif opcion == "2":
        sec_buscado = pedir_sector()
        print(f"\n--- PLANTAS EN SECTOR: {sec_buscado.upper()} ---")
        hubo_resultados = False
        for planta in plantas:
            if planta["sector"] == sec_buscado.lower():
                mostrar_planta(planta)
                hubo_resultados = True
        if not hubo_resultados:
            print("No hay plantas registradas en este sector.")
            
    elif opcion == "3":
        cat_buscada = pedir_categoria()
        print(f"\n--- PLANTAS EN CATEGORÍA: {cat_buscada.upper()} ---")
        hubo_resultados = False
        for planta in plantas:
            if planta["categoria"] == cat_buscada.lower():
                mostrar_planta(planta)
                hubo_resultados = True
        if not hubo_resultados:
            print("No hay plantas registradas en esta categoría.")
    else:
        print("Opción inválida. Volviendo al menú principal.")

def elegir_planta_de_lista(resultados):
    """
    Si hay una sola planta en la lista, la devuelve directamente.
    Si hay varias, muestra un menú numerado para que el usuario elija.
    Devuelve None si el usuario cancela.
    """
    if len(resultados) == 1:
        return resultados[0]
 
    print(f"\nSe encontraron {len(resultados)} plantas. Elija una:")
    for i, planta in enumerate(resultados, 1):
        print(f"  {i}. {planta['nombre_comun']} / {planta['nombre_cientifico']} (código identificador: {planta['id']})")
    print(f"  {len(resultados) + 1}. Cancelar")
 
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= len(resultados):
                return resultados[opcion - 1]
            elif opcion == len(resultados) + 1:
                print("  Operación cancelada.")
                return None
            else:
                print("  Opción inválida.")
        except ValueError:
            print("  Debe ingresar un número.")

def actualizar_stock_planta(plantas):
    if not plantas:
        print("\nEl inventario está vacío.")
        return
 
    # El usuario no conoce el código interno → primero busca por nombre
    busqueda = input("\nIngrese el nombre de la planta a actualizar: ")
    resultados = buscar_plantas_por_texto(plantas, busqueda)
 
    if not resultados:
        print("No se encontró ninguna planta con ese nombre.")
        return
 
    # Si hay más de un resultado, el usuario elige cuál
    planta = elegir_planta_de_lista(resultados)
    if planta is None:
        return
 
    print(f"\nPlanta seleccionada: {planta['nombre_comun']} (código identificador {planta['id']}) — Stock actual: {planta['stock']}")
 
    cantidad = pedir_entero("Ingrese la cantidad: ")
    motivo = pedir_motivo()
 
    if motivo == "reproduccion":
        planta["stock"] += cantidad
        print(f"  Éxito: Se sumaron {cantidad} unidades por reproducción. Stock actual: {planta['stock']}.")
 
    elif motivo == "venta" or motivo == "muerte":
        if cantidad <= planta["stock"]:
            planta["stock"] -= cantidad
            print(f"  Éxito: Se restaron {cantidad} unidades por {motivo}. Stock actual: {planta['stock']}.")
        else:
            print(f"  Error: Stock insuficiente. Disponible: {planta['stock']}.")


# 3 - Validaciones 
def pedir_string(mensaje):
    texto = input(mensaje).strip()
    while not texto:
        print("Error: Este campo no puede quedar vacío. Intente nuevamente.")
        texto = input(mensaje).strip()
    return texto

def pedir_entero(mensaje):
    """Pide un número entero no negativo."""
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("Error: el número no puede ser negativo.")
            else:
                return numero
        except ValueError:
            print("Error: debe ingresar un número entero.")


def pedir_float(mensaje):
    """Pide un número decimal no negativo."""
    while True:
        try:
            numero = float(input(mensaje))
            if numero < 0:
                print("Error: el precio no puede ser negativo.")
            else:
                return numero
        except ValueError:
            print("Error: debe ingresar un número válido.")


def pedir_categoria():
    """Muestra las categorías disponibles y devuelve la elegida como texto."""
    print("\nCategorías permitidas:\n1. Árbol\n2. Arbusto\n3. Suculenta\n4. Aromática\n5. Frutal\n6. Ornamental\n7. Otro")
    opcion = input("Seleccione una categoría: ")
    while opcion not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Error: opción incorrecta.")
        opcion = input("Seleccione una categoría nuevamente: ")
    
    categorias = {"1": "árbol", "2": "arbusto", "3": "suculenta", "4": "aromática", "5": "frutal", "6": "ornamental", "7": "otro"}
    return categorias[opcion]


def pedir_sector():
    """Muestra los sectores disponibles y devuelve el seleccionado por el usuario."""
    print("\nSectores permitidos:\n1. Interior\n2. Exterior\n3. Invernadero\n4. Huerta")
    opcion = input("Seleccione un sector: ")
    while opcion not in ["1", "2", "3", "4"]:
        print("Error: opción incorrecta.")
        opcion = input("Seleccione un sector nuevamente: ")
    
    sectores = {"1": "interior", "2": "exterior", "3": "invernadero", "4": "huerta"}
    return sectores[opcion]


def pedir_motivo():
    """Muestra los motivos de actualización y devuelve el elegido como texto."""
    print("\nMotivos permitidos:\n1. Reproduccion\n2. Venta\n3. Muerte")
    opcion = input("Seleccione un motivo: ")
    while opcion not in ["1", "2", "3"]:
        print("Error: opción incorrecta. Los motivos permitidos son: 1. Reproducción, 2. Venta, 3. Muerte:")
        opcion = input("Seleccione un motivo nuevamente: ")
    
    motivos = {"1": "reproduccion", "2": "venta", "3": "muerte"}
    return motivos[opcion].lower()

# vistas del menu
def cargar_planta():
    """Solicita al usuario los datos de una planta nueva y los devuelve como una tupla."""
    print("\n--- ALTA DE NUEVA PLANTA ---")
    
    nombre_comun = pedir_string("Nombre común: ")
    nombre_cientifico = pedir_string("Nombre científico: ")
    
    categoria = pedir_categoria()
    sector = pedir_sector()
    stock = pedir_entero("Cantidad en stock: ")
    precio = pedir_float("Precio unitario: ")
    
    cuidados = pedir_string("Cuidados básicos: ")
    
    return nombre_comun, nombre_cientifico, categoria, sector, stock, precio, cuidados
def buscar_planta(plantas):
    if not plantas:
        print("\nEl inventario está vacío.")
        return
    
    busqueda = input("\nIngrese nombre común o científico a buscar: ")
    resultados = buscar_plantas_por_texto(plantas, busqueda)
    
    if not resultados:
        print("No se encontró ninguna planta con ese nombre.")
    else:
        for planta in resultados:
            mostrar_planta(planta)

def eliminar_planta(plantas):
    if not plantas:
        print("\nEl inventario está vacío.")
        return
 
    # El usuario no conoce el id interno → primero busca por nombre
    busqueda = input("\nIngrese el nombre de la planta que desea eliminar: ")
    resultados = buscar_plantas_por_texto(plantas, busqueda)
 
    if not resultados:
        print("No se encontró ninguna planta con ese nombre.")
        return
 
    # Si hay más de un resultado, el usuario elige cuál
    planta = elegir_planta_de_lista(resultados)
    if planta is None:
        return
 
    print("\nPlanta a eliminar:")
    mostrar_planta(planta)                       
 
    confirmacion = input("¿Está seguro que desea eliminar esta planta? (s/n): ").lower()
    if confirmacion == "s":
        plantas.remove(planta)
        print("  Planta eliminada correctamente.")
    else:
        print("  Eliminación cancelada.")
        

def mostrar_planta(planta):
    print("\n--- DATOS DE LA PLANTA ---")
    print(f"ID: {planta['id']}")
    print(f"Nombre común: {planta['nombre_comun']}")
    print(f"Nombre científico: {planta['nombre_cientifico']}")
    print(f"Categoría: {planta['categoria']}")
    print(f"Sector: {planta['sector']}")
    print(f"Stock: {planta['stock']}")
    print(f"Precio unitario: ${planta['precio']:.2f}")
    print(f"Cuidados básicos: {planta['cuidados']}")
    print("---------------------------")
