"""Modulo 1: gestion de productos (alta, baja y consulta)."""


def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un producto al inventario. Si ya existe, suma la cantidad."""
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacio")
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa")

    clave = nombre.strip().lower()
    if clave in inventario:
        inventario[clave]["cantidad"] += cantidad
        inventario[clave]["precio"] = precio
    else:
        inventario[clave] = {"precio": precio, "cantidad": cantidad}
    return inventario


def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario."""
    clave = nombre.strip().lower()
    if clave not in inventario:
        raise KeyError(f"El producto '{nombre}' no existe")
    del inventario[clave]
    return inventario


def listar_productos(inventario):
    """Regresa la lista de productos ordenada alfabeticamente."""
    return sorted(inventario.keys())
