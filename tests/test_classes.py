from unittest.mock import patch

from src.classes import Category, Product

""" Тестирование класса Product """


# Проверка успешной инициализации экземпляра класса Product
def test_product_init(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 210000.0
    assert product_samsung.quantity == 5


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
def test_product_new_add(product_samsung, product_iphone, product_xiaomi_dict):
    len_before = len(Product.all_products)
    new_prod = Product.new_product(product_xiaomi_dict)
    len_after = len(Product.all_products)
    assert new_prod.name == "Xiaomi Redmi Note 11"
    assert new_prod.price == 31000.0
    assert new_prod.quantity == 14
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


""" Тестирование класса Category """


def test_category_init(first_category, second_category, product_samsung_2, product_iphone, product_xiaomi):
    # Проверка успешной инициализации экземпляра класса Category
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций"
    )
    assert len(first_category.products.split("\n")) - 1 == 3

    # Проверка успешной работы атрибута класса Category.category_count
    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert Category.category_count == 2

    # Проверка успешной работы атрибута класса Category.product_count
    assert first_category.product_count == 4
    assert second_category.product_count == 4
    assert Category.product_count == 4

    # Проверка добавления одного продукта
    second_category.add_product(product_samsung_2)
    lines = second_category.products.split("\n")
    count = len(lines) - 1
    assert count == 2
    assert second_category.products == (
        '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n' "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 10 шт.\n"
    )

    # Проверка добавления списка продуктов
    second_category.add_product([product_iphone, product_xiaomi])
    lines = second_category.products.split("\n")
    count = len(lines) - 1
    assert count == 4
    assert second_category.products == (
        '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 10 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )
