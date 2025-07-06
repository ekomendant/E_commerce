from typing import Any

from src.base_classes import BaseCategory
from src.product import Product


class Order(BaseCategory):
    """Класс для представления заказов."""

    def __init__(self, product: Product, quantity: int) -> None:
        """Метод для инициализации экземпляра класса заказов."""

        self.product = product
        self.quantity = quantity

    @property
    def amount(self) -> Any:
        """Метод для вычисления общей стоимости товаров в заказе."""

        return self.product.price * self.quantity

    def __str__(self) -> str:
        """Метод возвращает описание экземпляра класса заказов в виде строки"""

        return f"{self.product.name}, количество: {self.quantity} шт., сумма заказа: {self.amount} руб."
