class ZeroQuantity(Exception):
    """
    Класс исключения, отвечающий за обработку событий добавления товара с нулевым количеством в Категорию или заказ.
    """

    def __init__(self, message: str | None = None) -> None:
        """Инициализация класса"""

        super().__init__(message)
