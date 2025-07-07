from typing import Any

from src.base_classes import BaseCategory
from src.exception_class import ZeroQuantity
from src.product import Product


class Category(BaseCategory):
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
                    try:
                        if prod.quantity == 0:
                            raise ZeroQuantity(f"Нельзя добавить товар {prod.name} с нулевым количеством")
                    except ZeroQuantity as e:
                        print(str(e))
                    else:
                        self.__products.append(prod)
                        Category.product_count += 1
                        print(f"Товар {prod.name} успешно добавлен")
                    finally:
                        print("Добавление товара завершено")
        elif isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantity(f"Нельзя добавить товар {product.name} с нулевым количеством")
            except ZeroQuantity as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print(f"Товар {product.name} успешно добавлен")
            finally:
                print("Добавление товара завершено")
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

    @property
    def amount(self) -> Any:
        """Метод для вычисления общей стоимости товаров в категории."""

        total = 0.0
        for prod in self.__products:
            amount = prod.price * prod.quantity
            total += amount
        return total

    def middle_price(self) -> Any:
        """Метод для вычисления средней стоимости товаров в категории."""

        sum_product = 0.0
        for product in self.__products:
            sum_product += product.price

        try:
            avg = sum_product / len(self.__products)
            return round(avg, 2)
        except ZeroDivisionError:
            return 0
