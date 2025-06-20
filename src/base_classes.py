from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный родительский класс для продуктов."""

    @classmethod
    @abstractmethod  # pragma: no cover
    def new_product(cls, *args: Any, **kwargs: Any) -> None:
        """Абстрактный метод для добавления нового экземпляра класса."""

        pass


class BaseCategory(ABC):
    """Абстрактный родительский класс для категорий товаров и заказов."""

    @abstractmethod  # pragma: no cover
    def amount(self, *args: Any, **kwargs: Any) -> None:
        """Абстрактный метод для вычисления общей стоимости товаров в категории или заказе."""

        pass
