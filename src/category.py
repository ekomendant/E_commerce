from src.product import Product


class Category:
    """Класс для представления категорий товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Метод для инициализации экземпляра класса категорий товаров."""

        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """Метод возвращает описание экземпляра класса категорий в виде строки"""

        total = 0
        for prod in self.__products:
            total += prod.quantity
        return f"{self.name}, количество продуктов: {total} шт."

    def add_product(self, product: list | Product) -> None:
        """Метод для добавления новых продуктов в список products"""

        if isinstance(product, list):
            for prod in product:
                if isinstance(prod, Product):
                    self.__products.append(prod)
                    Category.product_count += 1
        elif isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        """Метод-геттер для получения списка продуктов выбранной категории в виде строки"""

        product_str = ""
        for prod in self.__products:
            product_str += f"{str(prod)}\n"
        return product_str

    @property
    def products_list(self) -> list:
        """Метод-геттер для получения списка продуктов выбранной категории"""

        return self.__products
