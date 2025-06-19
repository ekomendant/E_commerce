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

    def __str__(self) -> str:
        """Метод возвращает описание экземпляра класса товаров в виде строки"""

        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

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

    def __add__(self, other: "Product") -> float:
        """Метод рассчитывает общую стоимость (цена * количество) двух продуктов одного дочернего класса"""

        if type(self) is type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError
