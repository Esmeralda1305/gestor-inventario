from app.reportes import generar_reporte


def test_reporte_contiene_total():
    inv = {"teclado": {"precio": 250.0, "cantidad": 2}}
    reporte = generar_reporte(inv)
    assert "Valor total: $500.00" in reporte


def test_reporte_bajo_stock():
    inv = {"mouse": {"precio": 100.0, "cantidad": 1}}
    assert "Bajo stock: mouse" in generar_reporte(inv)
