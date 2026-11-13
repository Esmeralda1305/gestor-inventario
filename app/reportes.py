"""Modulo 3: generacion de reportes de texto."""

from app.calculos import valor_total, productos_bajo_stock


def generar_reporte(inventario, minimo=5):
    """Genera un reporte en texto con el resumen del inventario."""
    lineas = ["REPORTE DE INVENTARIO", "-" * 21]
    for nombre in sorted(inventario):
        p = inventario[nombre]
        lineas.append(f"{nombre}: {p['cantidad']} pzs x ${p['precio']:.2f}")
    lineas.append(f"Valor total: ${valor_total(inventario):.2f}")
    bajos = productos_bajo_stock(inventario, minimo)
    lineas.append("Bajo stock: " + (", ".join(bajos) if bajos else "ninguno"))
    return "\n".join(lineas)
