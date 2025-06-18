from unittest.mock import patch

from src.product import Product


# Проверка успешной инициализации экземпляра класса Product
def test_product_init(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 210000.0
    assert product_samsung.quantity == 5
    assert str(product_samsung) == "Samsung Galaxy S23 Ultra, 210000.0 руб. Остаток: 5 шт."


# Проверка добавления нового экземпляра класса Product, если такое наименование уже существует
def test_product_new_not_add(product_samsung, product_iphone, product_samsung_dict):
    len_before = len(Product.all_products)
    new_prod = Product.new_product(product_samsung_dict)
    len_after = len(Product.all_products)
    assert new_prod.name == "Samsung Galaxy S23 Ultra"
    assert new_prod.price == 210000.0
    assert new_prod.quantity == 10
    assert len_before == len_after


# Проверка добавления нового экземпляра класса Product, если такого наименования еще нет
def test_product_new_add(product_samsung, product_iphone, product_realme_dict):
    len_before = len(Product.all_products)
    new_prod = Product.new_product(product_realme_dict)
    len_after = len(Product.all_products)
    assert new_prod.name == "REALME 14T 5G"
    assert new_prod.price == 20000.0
    assert new_prod.quantity == 20
    assert len_after - len_before == 1


# Проверка попытки изменения цены продукта (цена ниже текущей, пользователь не подтверждает изменение)
@patch("builtins.input")
def test_product_new_price_no(mock_input, product_samsung):
    mock_input.return_value = "NO"
    assert product_samsung.price == 210000.0
    product_samsung.price = 800
    assert product_samsung.price == 210000.0


# Проверка попытки изменения цены продукта (цена ниже текущей, пользователь подтверждает изменение)
@patch("builtins.input")
def test_product_new_price_yes(mock_input, product_samsung):
    mock_input.return_value = "YES"
    assert product_samsung.price == 210000.0
    product_samsung.price = 800
    assert product_samsung.price == 800.0


# Проверка попытки изменения цены продукта (цена выше текущей)
def test_product_new_price_up(product_samsung):
    assert product_samsung.price == 210000.0
    product_samsung.price = 350000.0
    assert product_samsung.price == 350000.0


# Проверка попытки изменения цены продукта (цена не положительная)
def test_product_new_price_minus(capsys, product_samsung):
    assert product_samsung.price == 210000.0

    product_samsung.price = 0.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product_samsung.price = -100.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


# Проверка сложения продуктов (вычисления общей стоимости)
def test_product_add(product_samsung, product_iphone, product_xiaomi):
    assert product_samsung + product_iphone == 2730000.0
    assert product_samsung + product_xiaomi == 1484000.0
    assert product_xiaomi + product_iphone == 2114000.0
