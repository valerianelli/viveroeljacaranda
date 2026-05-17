from encargos.encargos import registrar_encargo, cambiar_estado, eliminar_encargo_fisico

def correr_tests():
    print("Corriendo pruebas unitarias de 'Encargos'...")
    
    # Lista de prueba (simula la del main)
    encargos_test = []

    # 1. Test Registro
    res = registrar_encargo(encargos_test, 10, 5, "Palmera", 1, 2000.0)
    assert type(res) == dict
    assert len(encargos_test) == 1
    assert encargos_test[0]["id"] == 1
    print("  - Test Registro y ID: OK")

    # 2. Test Autoincremento
    registrar_encargo(encargos_test, 11, 2, "Rosal", 2, 500.0)
    assert encargos_test[1]["id"] == 2
    print("  - Test Autoincremento: OK")

    # 3. Test Cambio de Estado
    cambiar_estado(encargos_test, 1, "llegó")
    assert encargos_test[0]["estado"] == "llegó"
    print("  - Test Cambio Estado: OK")

    # 4. Test Validación de Tipos
    error = registrar_encargo(encargos_test, "texto", 5, "Error", "muchos", 0)
    assert type(error) == str
    print("  - Test Validaciones: OK")

    # 5. Test Eliminación
    eliminar_encargo_fisico(encargos_test, 1)
    assert len(encargos_test) == 1
    assert encargos_test[0]["id"] == 2
    print("  - Test Eliminación: OK")

    print("\n¡TODAS LAS PRUEBAS PASARON!")

if __name__ == "__main__":
    correr_tests()
