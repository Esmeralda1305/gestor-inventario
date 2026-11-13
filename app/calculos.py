"""Modulo 2: calculos sobre el inventario."""


def valor_total(inventario):
    """Calcula el valor total del inventario (precio x cantidad)."""
    return sum(p["precio"] * p["cantidad"] for p in inventario.values())


def productos_bajo_stock(inventario, minimo=5):
    """Regresa los productos cuya cantidad es menor al minimo."""
    return sorted(n for n, p in inventario.items() if p["cantidad"] < minimo)
