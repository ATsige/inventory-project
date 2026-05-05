def can_reduce_stock(current_stock, quantity):
    return quantity <= current_stock


def test_can_reduce_stock_true():
    assert can_reduce_stock(10, 5) is True


def test_can_reduce_stock_false():
    assert can_reduce_stock(3, 5) is False
    