from src.order import Order


def test_order(product_samsung):
    order = Order(product_samsung, 4)

    assert order.product == product_samsung
    assert order.quantity == 4
    assert order.amount == 840000.0
    assert str(order) == "Samsung Galaxy S23 Ultra, количество: 4 шт., сумма заказа: 840000.0 руб."
