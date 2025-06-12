import pytest

from src.classes import Category, Product


@pytest.fixture
def first_category(product_samsung, product_iphone, product_xiaomi):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций",
        products=[
            product_samsung,
            product_iphone,
            product_xiaomi,
        ],
    )


@pytest.fixture
def second_category(product_tv):
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом",
        products=[
            product_tv,
        ],
    )


@pytest.fixture
def product_samsung():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def product_iphone():
    return Product(
        name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8
    )


@pytest.fixture
def product_xiaomi():
    return Product(
        name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=14
    )


@pytest.fixture
def product_tv():
    return Product(
        name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7
    )


@pytest.fixture
def category_from_json():
    return [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        }
    ]
