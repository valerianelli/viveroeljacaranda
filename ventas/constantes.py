from datetime import date
import re

FORMAS_PAGO = ("efectivo", "transferencia", "tarjeta")
SEPARADOR = "-" * 51


def parsear_fecha(entrada):
    """
    Convierte un string de fecha en un objeto date.
    Acepta múltiples formatos: dd/mm/yyyy, yyyy-mm-dd, '15 de 05 de 2024', etc.
    Retorna un objeto date o None si la entrada es inválida.
    """
    partes = re.split(r"[/\-_|.,:;#]|\s+del?\s+|\s+", entrada)
    if len(partes) != 3:
        return None
    return _construir_fecha(partes)


def _construir_fecha(partes):
    """
    Recibe una lista de 3 strings numéricos y construye un objeto date.
    Detecta automáticamente si el año va primero o último.
    Retorna un objeto date o None si los valores son inválidos.
    """
    try:
        partes = [int(p) for p in partes]
    except ValueError:
        print("La fecha solo puede contener números, intente de nuevo...")
        return None

    anio = max(partes)
    if len(str(anio)) != 4:
        print("El año debe tener 4 dígitos, intente de nuevo...")
        return None

    pos_anio = partes.index(anio)
    mes = partes[1]
    dia = partes[0] if pos_anio == 2 else partes[2]

    if not 1 <= mes <= 12:
        print("El mes debe ser un número entre 1 y 12, intente de nuevo...")
        return None
    if not 1 <= dia <= 31:
        print("El día debe ser un número entre 1 y 31, intente de nuevo...")
        return None

    try:
        return date(anio, mes, dia)
    except ValueError:
        print("La fecha ingresada no es válida, intente de nuevo...")
        return None


def buscar_por_id(lista, id_buscado):
    """Retorna el primer elemento de la lista cuyo campo 'id' coincida, o None."""
    for elemento in lista:
        if elemento["id"] == id_buscado:
            return elemento
    return None


def pedir_confirmacion(mensaje="¿Confirmar? (si/no): "):
    """
    Solicita confirmación al usuario en un loop hasta recibir 'si' o 'no'.
    Retorna True si confirma, False si cancela.
    """
    while True:
        respuesta = input(f"\n{mensaje}").lower()
        if respuesta == "si":
            return True
        if respuesta == "no":
            return False
        print("Opción inválida, ingrese 'si' o 'no'...")


def imprimir_exito(mensaje):
    print()
    print(SEPARADOR)
    print(mensaje.center(51))
    print(SEPARADOR)
