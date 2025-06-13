from typing import Any


class Product:
    """Класс для представления товаров."""

    all_products: list = []
    all_names: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса товаров."""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.all_products.append(self)
        Product.all_names.append(self.name)

    @classmethod
    def new_product(cls, product: dict) -> Any:
        """
        Метод для добавления нового экземпляра класса, переданного в виде словаря, с проверкой на дублирование продукта
        """

        if product["name"] in cls.all_names:
            result = 0
            for prod in cls.all_products:
                if product["name"] == prod.name:
                    prod.quantity += product["quantity"]
                    prod.__price = max(prod.__price, product["price"])
                    result = prod
                    break
            return result
        else:
            return cls(**product)

    @property
    def price(self) -> float:
        """Метод-геттер для получения цены продукта"""

        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Метод-сеттер для изменения цены продукта"""

        if new_price > 0:
            if new_price < self.__price:
                confirmation = input(
                    f"Текущая цена {self.__price}, вы указываете цену ниже {new_price}. "
                    f"Понизить цену товара? Введите YES или NO: "
                )
                if confirmation.lower() == "yes":
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


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

    @property
    def products(self) -> str:
        """Метод-геттер для получения списка продуктов выбранной категории в виде строки"""

        product_str = ""
        for prod in self.__products:
            product_str += f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
        return product_str
