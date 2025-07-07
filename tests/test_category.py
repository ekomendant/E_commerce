import pytest

from src.category import Category


# Проверка инициализации категории
def test_category_init(first_category, second_category):
    # Проверка успешной инициализации экземпляра класса Category
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций"
    )
    assert len(first_category.products.split("\n")) - 1 == 3
    assert len(first_category.products_list) == 3

    # Проверка строкового отображения категории
    assert str(first_category) == "Смартфоны, количество продуктов: 27 шт."

    # Проверка успешной работы атрибута класса Category.category_count
    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert Category.category_count == 2

    # Проверка успешной работы атрибута класса Category.product_count
    assert first_category.product_count == 4
    assert second_category.product_count == 4
    assert Category.product_count == 4


# Проверка добавления продуктов в категорию
def test_category_add(first_category, second_category, product_samsung_2, product_iphone, product_xiaomi):
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

    # Проверка добавления объекта отличного от класса Product
    with pytest.raises(TypeError):
        second_category.add_product("Смартфон")

    # Проверка расчета общей стоимости товаров в категории
    assert first_category.amount == 3164000.0


# Проверка расчета средней стоимости товаров в категории
def test_category_middle(first_category, empty_category):
    # Если категория содержит товары
    assert first_category.middle_price() == 150333.33

    # Если категория не содержит товары
    assert empty_category.middle_price() == 0
