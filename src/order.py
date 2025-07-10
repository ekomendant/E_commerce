from typing import Any

from src.base_classes import BaseCategory
from src.exception_class import ZeroQuantity
from src.product import Product


class Order(BaseCategory):
    """Класс для представления заказов."""

    def __init__(self, product: Product, quantity: int) -> None:
        """Метод для инициализации экземпляра класса заказов."""

        try:
            if quantity == 0:
                raise ZeroQuantity(f"Нельзя добавить товар {product.name} с нулевым количеством")
        except ZeroQuantity as e:
            print(str(e))
        else:
            self.product = product
            self.quantity = quantity
            print(f"Товар {product.name} успешно добавлен")
        finally:
            print("Добавление товара завершено")

    @property
    def amount(self) -> Any:
        """Метод для вычисления общей стоимости товаров в заказе."""

        return self.product.price * self.quantity

    def __str__(self) -> str:
        """Метод возвращает описание экземпляра класса заказов в виде строки"""

        return f"{self.product.name}, количество: {self.quantity} шт., сумма заказа: {self.amount} руб."
