class Product:
    """Класс для представления товаров."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса товаров."""

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категорий товаров."""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Метод для инициализации экземпляра класса категорий товаров."""

        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(self.products)
