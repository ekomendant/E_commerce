from typing import Any

from src.category import Category


class ProductIterator:
    """Вспомогательный класс для поочередного вывода продуктов одной категории."""

    def __init__(self, category_object: Category) -> None:
        """Метод для инициализации экземпляра класса ProductIterator."""

        self.category = category_object
        self.index = 0

    def __iter__(self) -> "ProductIterator":
        """Метод для получения итератора для перебора объекта."""

        return self

    def __next__(self) -> Any:
        """Метод для получения следующего значения итератора."""

        if self.index < len(self.category.products_list):
            product = self.category.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
