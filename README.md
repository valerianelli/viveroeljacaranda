# 🌱 Vivero El Jacarandá — Sistema de Gestión v1.0

Sistema de gestión integral para vivero, desarrollado como Trabajo Práctico Integrador de Programación 1 — UNER.

---

## 👥 Integrantes

| Nombre | 
|---|
| Valeria Nelli |
| Ariel Guas |
| Luciano Maciel |
| Eliana Jovanovich |
| Miguel Casaretto |

---

## 📋 Descripción

Aplicación de consola en Python para administrar las operaciones diarias de un vivero: stock de plantas, clientes, ventas, proveedores y encargos especiales. Los datos se persisten en archivos JSON entre sesiones.

---

## 🗂️ Estructura del proyecto

```
vivero/
├── main.py                  # Punto de entrada y menú principal
├── archivos/
│   ├── persistencia.py      # Carga y guardado de datos en JSON
│   └── *.json               # Archivos de datos (generados al ejecutar)
├── stock/
│   ├── stock.py             # Lógica de inventario de plantas
│   └── menu_stock.py        # Menú de stock
├── clientes/
│   ├── clientes.py          # Lógica de clientes
│   └── menu_clientes.py     # Menú de clientes
├── ventas/
│   ├── operaciones.py       # Registro, modificación y eliminación de ventas
│   ├── visualizacion.py     # Impresión de ventas
│   ├── inputs.py            # Validación de entradas del usuario
│   ├── constantes.py        # Utilidades compartidas
│   └── menu.py              # Menú de ventas
├── proveedores/
│   ├── proveedores.py       # Lógica de proveedores
│   └── menu_proveedores.py  # Menú de proveedores
└── encargos/
    ├── encargos.py          # Lógica de encargos especiales
    ├── menu_encargos.py     # Menú de encargos
    └── test_encargos.py     # Tests unitarios
```

---

## ⚙️ Funcionalidades

### 🌿 Stock de plantas
- Alta, baja y búsqueda de plantas (por nombre común o científico)
- Listado con filtros por sector (Interior, Exterior, Invernadero, Huerta) o categoría (Árbol, Arbusto, Suculenta, etc.)
- Actualización de stock por reproducción, venta o muerte

### 👤 Clientes
- Registro con DNI, nombre, teléfono, email opcional y tipo (Particular, Paisajista, Empresa, Vivero amigo)
- Búsqueda por DNI o nombre
- Modificación y eliminación con confirmación

### 💰 Ventas
- Registro de ventas con múltiples plantas, descuento automático de stock
- Soporte para efectivo, transferencia y tarjeta
- Búsqueda por DNI de cliente o fecha
- Modificación y eliminación con restauración de stock

### 🚚 Proveedores
- Registro con nombre, contacto, localidad, productos y fecha de último pedido
- Búsqueda por nombre o tipo de producto
- Actualización y eliminación

### 📦 Encargos especiales
- Registro de encargos vinculados a cliente y proveedor existentes
- Seguimiento de estado: `pedido` → `llegó` → `entregado` / `cancelado`
- Listado de encargos activos y búsqueda por cliente
- Baja con confirmación

---

## 🚀 Ejecución

**Requisitos:** Python 3.10 o superior (se usa `match/case`).

```bash
# Ejecutar el sistema principal
python3 main.py

# Ejecutar los tests de encargos
python3 encargos/test_encargos.py
```

---

## 💾 Persistencia de datos

Los datos se guardan automáticamente al salir del sistema (opción `0` del menú principal) en archivos JSON dentro de la carpeta `archivos/`:

- `plantas.json`
- `clientes.json`
- `ventas.json`
- `proveedores.json`
- `encargos.json`

> Los archivos JSON están excluidos del repositorio por el `.gitignore`. Al ejecutar el sistema por primera vez, se crearán automáticamente.
