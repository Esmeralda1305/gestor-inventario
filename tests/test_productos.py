import pytest
from app.productos import agregar_producto, eliminar_producto, listar_productos


def test_agregar_producto_nuevo():
    inv = {}
    agregar_producto(inv, "Teclado", 250, 10)
    assert inv["teclado"] == {"precio": 250, "cantidad": 10}


def test_agregar_producto_existente_suma_cantidad():
    inv = {}
    agregar_producto(inv, "Teclado", 250, 10)
    agregar_producto(inv, "teclado", 250, 5)
    assert inv["teclado"]["cantidad"] == 15


def test_agregar_precio_negativo_falla():
    with pytest.raises(ValueError):
        agregar_producto({}, "Mouse", -1, 1)


def test_eliminar_producto():
    inv = {}
    agregar_producto(inv, "Mouse", 100, 2)
    eliminar_producto(inv, "Mouse")
    assert listar_productos(inv) == []


def test_eliminar_inexistente_falla():
    with pytest.raises(KeyError):
        eliminar_producto({}, "Nada")
