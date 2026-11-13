from app.productos import agregar_producto, eliminar_producto
from app.reportes import generar_reporte


def main():
    inventario = {}
    agregar_producto(inventario, "Teclado", 250.0, 10)
    agregar_producto(inventario, "Mouse", 120.5, 3)
    agregar_producto(inventario, "Monitor", 2400.0, 2)
    eliminar_producto(inventario, "Mouse")
    print(generar_reporte(inventario))


if __name__ == "__main__":
    main()
