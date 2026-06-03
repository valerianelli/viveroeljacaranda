from encargos import (
    registrar_encargo, cambiar_estado, eliminar_encargo,
    buscar_por_cliente, buscar_por_proveedor, buscar_por_fecha
)


def correr_tests():
    print("Corriendo pruebas unitarias de 'Encargos'...")

    encargos_test = []

    fecha = "2026-06-15"

    # 1. Test Registro
    res = registrar_encargo(encargos_test, 10, 5, "Palmera", 1, 2000.0, fecha)
    assert type(res) == dict
    assert len(encargos_test) == 1
    assert encargos_test[0]["id"] == 1
    assert encargos_test[0]["estado"] == "pedido"
    print("  - Test Registro y ID: OK")

    # 2. Test Autoincremento
    registrar_encargo(encargos_test, 11, 2, "Rosal", 2, 500.0, fecha)
    assert encargos_test[1]["id"] == 2
    print("  - Test Autoincremento: OK")

    # 3. Test Cambio de Estado
    cambiar_estado(encargos_test, 1, "llegó")
    assert encargos_test[0]["estado"] == "llegó"
    print("  - Test Cambio Estado: OK")

    # 4. Test Búsqueda por cliente
    resultados = buscar_por_cliente(encargos_test, 10)
    assert len(resultados) == 1
    assert resultados[0]["id"] == 1
    print("  - Test Búsqueda por cliente: OK")

    # 5. Test Búsqueda por proveedor
    resultados = buscar_por_proveedor(encargos_test, 2)
    assert len(resultados) == 1
    assert resultados[0]["id"] == 2
    print("  - Test Búsqueda por proveedor: OK")

    # 6. Test Búsqueda por fecha
    resultados = buscar_por_fecha(encargos_test, fecha)
    assert len(resultados) == 2
    print("  - Test Búsqueda por fecha: OK")

    # 7. Test Eliminación
    eliminar_encargo(encargos_test, 1)
    assert len(encargos_test) == 1
    assert encargos_test[0]["id"] == 2
    print("  - Test Eliminación: OK")

    print("\n¡TODAS LAS PRUEBAS PASARON!")


if __name__ == "__main__":
    correr_tests()
