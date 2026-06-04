from encargos import (
    registrar_encargo, cambiar_estado, eliminar_encargo,
    buscar_por_cliente, buscar_por_proveedor, buscar_por_fecha,
    generar_proximo_id, obtener_cliente_por_id, obtener_proveedor_por_id,
    dame_activos
)


def correr_tests():
    print("Corriendo pruebas unitarias de 'Encargos'...")
    fallaron = 0

    fecha = "2026-06-15"

    # 1. generar_proximo_id con lista vacía
    assert generar_proximo_id([]) == 1
    print("  - Test generar_proximo_id vacío: OK")

    # 2. Registrar encargo y verificar todos los campos
    encargos_test = []
    res = registrar_encargo(encargos_test, 10, 5, "Palmera", 1, 2000.0, fecha)
    assert type(res) == dict
    assert len(encargos_test) == 1
    assert res["id"] == 1
    assert res["id_cliente"] == 10
    assert res["id_proveedor"] == 5
    assert res["descripcion"] == "Palmera"
    assert res["cantidad"] == 1
    assert res["sena"] == 2000.0
    assert res["estado"] == "pedido"
    assert res["fecha_estimada_llegada"] == fecha
    assert type(res["fecha_pedido"]) == str
    print("  - Test Registro campos completos: OK")

    # 3. Autoincremento de ID
    res2 = registrar_encargo(encargos_test, 11, 2, "Rosal", 2, 500.0, fecha)
    assert res2["id"] == 2
    assert encargos_test[1]["id"] == 2
    print("  - Test Autoincremento ID: OK")

    # 4. Estado inicial es "pedido"
    assert encargos_test[0]["estado"] == "pedido"
    assert encargos_test[1]["estado"] == "pedido"
    print("  - Test Estado inicial pedido: OK")

    # 5. Cambiar estado: pedido -> llegó
    assert cambiar_estado(encargos_test, 1, "llegó") == True
    assert encargos_test[0]["estado"] == "llegó"
    print("  - Test Cambio estado a llegó: OK")

    # 6. Cambiar estado: llegó -> entregado
    assert cambiar_estado(encargos_test, 1, "entregado") == True
    assert encargos_test[0]["estado"] == "entregado"
    print("  - Test Cambio estado a entregado: OK")

    # 7. Cambiar estado a cancelado
    assert cambiar_estado(encargos_test, 2, "cancelado") == True
    assert encargos_test[1]["estado"] == "cancelado"
    print("  - Test Cambio estado a cancelado: OK")

    # 8. cambiar_estado con ID inexistente devuelve False
    assert cambiar_estado(encargos_test, 999, "entregado") == False
    print("  - Test Cambio estado ID inexistente: OK")

    # 9. eliminar_encargo existente
    assert eliminar_encargo(encargos_test, 1) == True
    assert len(encargos_test) == 1
    assert encargos_test[0]["id"] == 2
    print("  - Test Eliminación: OK")

    # 10. eliminar_encargo con ID inexistente devuelve False
    assert eliminar_encargo(encargos_test, 999) == False
    assert len(encargos_test) == 1
    print("  - Test Eliminación ID inexistente: OK")

    # 11. Búsqueda por cliente - encuentra
    encargos_test.clear()
    registrar_encargo(encargos_test, 10, 5, "Palmera", 1, 2000.0, fecha)
    registrar_encargo(encargos_test, 10, 2, "Rosal", 2, 500.0, fecha)
    registrar_encargo(encargos_test, 20, 5, "Limonero", 1, 1500.0, fecha)
    resultados = buscar_por_cliente(encargos_test, 10)
    assert len(resultados) == 2
    assert resultados[0]["id"] == 1
    assert resultados[1]["id"] == 2
    print("  - Test Búsqueda por cliente encuentra: OK")

    # 12. Búsqueda por cliente - sin resultados
    resultados = buscar_por_cliente(encargos_test, 999)
    assert resultados == []
    print("  - Test Búsqueda por cliente sin resultados: OK")

    # 13. Búsqueda por proveedor - encuentra
    resultados = buscar_por_proveedor(encargos_test, 5)
    assert len(resultados) == 2
    assert resultados[0]["id"] == 1
    assert resultados[1]["id"] == 3
    print("  - Test Búsqueda por proveedor encuentra: OK")

    # 14. Búsqueda por proveedor - sin resultados
    resultados = buscar_por_proveedor(encargos_test, 999)
    assert resultados == []
    print("  - Test Búsqueda por proveedor sin resultados: OK")

    # 15. Búsqueda por fecha - encuentra (fecha_estimada_llegada)
    resultados = buscar_por_fecha(encargos_test, fecha)
    assert len(resultados) == 3
    print("  - Test Búsqueda por fecha encuentra: OK")

    # 16. Búsqueda por fecha - sin resultados
    resultados = buscar_por_fecha(encargos_test, "2099-01-01")
    assert resultados == []
    print("  - Test Búsqueda por fecha sin resultados: OK")

    # 17. Búsqueda por fecha_pedido (hoy)
    from datetime import date
    hoy = str(date.today())
    resultados = buscar_por_fecha(encargos_test, hoy)
    assert len(resultados) == 3
    print("  - Test Búsqueda por fecha_pedido (hoy): OK")

    # 18. obtener_cliente_por_id - encuentra
    clientes_mock = [
        {"id": 1, "nombre_completo": "Juan Perez", "telefono": "123456", "email": "juan@test.com"},
        {"id": 2, "nombre_completo": "Maria Garcia", "telefono": "789012", "email": ""}
    ]
    cliente = obtener_cliente_por_id(1, clientes_mock)
    assert cliente is not None
    assert cliente["nombre_completo"] == "Juan Perez"
    print("  - Test obtener_cliente_por_id encuentra: OK")

    # 19. obtener_cliente_por_id - no encuentra
    assert obtener_cliente_por_id(999, clientes_mock) is None
    print("  - Test obtener_cliente_por_id sin resultados: OK")

    # 20. obtener_cliente_por_id - lista vacía
    assert obtener_cliente_por_id(1, []) is None
    print("  - Test obtener_cliente_por_id lista vacía: OK")

    # 21. obtener_proveedor_por_id - encuentra
    proveedores_mock = [
        {"id": 1, "nombre": "Vivero Central", "telefono": "111222"},
        {"id": 2, "nombre": "Plantas del Sur", "telefono": "333444"}
    ]
    proveedor = obtener_proveedor_por_id(2, proveedores_mock)
    assert proveedor is not None
    assert proveedor["nombre"] == "Plantas del Sur"
    print("  - Test obtener_proveedor_por_id encuentra: OK")

    # 22. obtener_proveedor_por_id - no encuentra
    assert obtener_proveedor_por_id(999, proveedores_mock) is None
    print("  - Test obtener_proveedor_por_id sin resultados: OK")

    # 23. dame_activos - filtra entregados y cancelados
    cambiar_estado(encargos_test, 1, "entregado")
    cambiar_estado(encargos_test, 2, "cancelado")
    activos = dame_activos(encargos_test)
    assert len(activos) == 1
    assert activos[0]["id"] == 3
    assert activos[0]["estado"] == "pedido"
    print("  - Test dame_activos filtra entregado/cancelado: OK")

    # 24. dame_activos - todos activos
    encargos_test.clear()
    registrar_encargo(encargos_test, 10, 5, "Planta A", 1, 0.0, fecha)
    registrar_encargo(encargos_test, 10, 5, "Planta B", 1, 0.0, fecha)
    activos = dame_activos(encargos_test)
    assert len(activos) == 2
    print("  - Test dame_activos todos activos: OK")

    # 25. dame_activos - ninguno activo
    cambiar_estado(encargos_test, 1, "entregado")
    cambiar_estado(encargos_test, 2, "cancelado")
    activos = dame_activos(encargos_test)
    assert activos == []
    print("  - Test dame_activos ninguno activo: OK")

    # 26. dame_activos - lista vacía
    assert dame_activos([]) == []
    print("  - Test dame_activos lista vacía: OK")

    # 27. Seña = 0 es válido
    res_sena_cero = registrar_encargo(encargos_test, 10, 5, "Prueba", 1, 0.0, fecha)
    assert res_sena_cero["sena"] == 0.0
    print("  - Test seña cero válida: OK")

    # 28. Fecha estimada distinta
    fecha2 = "2026-07-20"
    res_fecha2 = registrar_encargo(encargos_test, 10, 5, "Otra", 1, 100.0, fecha2)
    assert res_fecha2["fecha_estimada_llegada"] == fecha2
    resultados = buscar_por_fecha(encargos_test, fecha2)
    assert len(resultados) == 1
    assert resultados[0]["descripcion"] == "Otra"
    print("  - Test fecha estimada distinta: OK")

    # 29. Cantidad > 1
    res_multi = registrar_encargo(encargos_test, 10, 5, "Multi", 10, 500.0, fecha)
    assert res_multi["cantidad"] == 10
    print("  - Test cantidad mayor a 1: OK")

    print("\n¡TODAS LAS PRUEBAS PASARON!")


if __name__ == "__main__":
    correr_tests()
