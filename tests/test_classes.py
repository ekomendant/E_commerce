from src.classes import Category


def test_product_init(product_samsung):
    # Проверка успешной инициализации экземпляра класса Product
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_category_init(first_category, second_category):
    # Проверка успешной инициализации экземпляра класса Category
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций"
    )
    assert len(first_category.products) == 3

    # Проверка успешной работы атрибута класса Category.category_count
    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert Category.category_count == 2

    # Проверка успешной работы атрибута класса Category.product_count
    assert first_category.product_count == 4
    assert second_category.product_count == 4
    assert Category.product_count == 4
