from app.calculos import valor_total, productos_bajo_stock


def test_valor_total():
    inv = {"a": {"precio": 10, "cantidad": 2}, "b": {"precio": 5, "cantidad": 4}}
    assert valor_total(inv) == 40


def test_valor_total_vacio():
    assert valor_total({}) == 0


def test_productos_bajo_stock():
    inv = {"a": {"precio": 1, "cantidad": 2}, "b": {"precio": 1, "cantidad": 9}}
    assert productos_bajo_stock(inv) == ["a"]
