from src.order import Order


def test_order(product_samsung):
    order = Order(product_samsung, 4)

    assert order.product == product_samsung
    assert order.quantity == 4
    assert order.amount == 840000.0
    assert str(order) == "Samsung Galaxy S23 Ultra, количество: 4 шт., сумма заказа: 840000.0 руб."


# Проверка добавления продуктов в категорию
def test_order_exception(capsys, product_iphone):
    # Добавление в заказ товара с нулевым количеством
    Order(product_iphone, 0)
    messages = capsys.readouterr()
    assert messages.out.strip().split("\n")[-2] == "Нельзя добавить товар Iphone 15 с нулевым количеством"
    assert messages.out.strip().split("\n")[-1] == "Добавление товара завершено"

    # Добавление в заказ товара с ненулевым количеством
    Order(product_iphone, 2)
    messages = capsys.readouterr()
    assert messages.out.strip().split("\n")[-2] == "Товар Iphone 15 успешно добавлен"
    assert messages.out.strip().split("\n")[-1] == "Добавление товара завершено"
