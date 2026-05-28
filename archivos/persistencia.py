import json

def cargar_datos(nombre_archivo):
    """
    Retorna los datos guardados en el archivo especificado por parametro.
    Si el archivo existe, retorna los datos del mismo.
    Si el archivo no existe, retorna una lista vacia.
    """
    try:
        nombre_archivo = nombre_archivo.lower()
        with open(f"archivos/{nombre_archivo}.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(datos, nombre_archivo):
    """
    Guarda los datos pasados en el primer parametro, en el archivo
    con el nombre correspondiente al segundo parametro.
    Se asegura que el nombre del archivo pasado deba coincidir con
    "ventas", "encargos", "clientes", "plantas" o "proveedores".
    Si el nombre pasado no coincide con los esperados, no hace nada.
    Si el archivo no existe, lo crea y guarda los datos.
    Si el archivo ya existia, remplaza todos sus datos con los nuevos.
    """
    nombre_archivo = nombre_archivo.lower()
    if nombre_archivo in ("ventas", "encargos", "clientes", "plantas", "proveedores"):
        with open(f"archivos/{nombre_archivo}.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo)
