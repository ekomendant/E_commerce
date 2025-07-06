class Mixin:

    def __init__(self) -> None:
        """Метод для инициализации экземпляра класса."""

        print(repr(self))

    def __repr__(self) -> str:
        """Метод для вывода в консоль информации о классе и параметрах созданного объекта."""

        name = self.__dict__["name"]
        description = self.__dict__["description"]
        price = self.__dict__["_Product__price"]
        quantity = self.__dict__["quantity"]
        return f"{self.__class__.__name__}('{name}', '{description}', {price}, {quantity})"
