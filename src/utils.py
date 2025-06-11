import json
from json import JSONDecodeError
from typing import Any

from src.classes import Category, Product


def read_json(file_json: str) -> Any:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными.
    :param file_json: Путь до JSON-файла.
    :return: Список словарей с данными файла.
    """

    try:
        with open(file_json, "r", encoding="utf-8") as json_file:
            try:
                info = json.load(json_file)
                return info
            except JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


def create_objects_from_json(data: list) -> list:
    """
    Функция принимает список словарей и преобразовывает данные в объекты классов
    :param data: список словарей с данными
    :return: список с объектами классов
    """

    if isinstance(data, list) and len(data) > 0:
        categories = []
        for category in data:
            products = []
            for product in category["products"]:
                products.append(Product(**product))
            category["products"] = products
            categories.append(Category(**category))
        return categories
    else:
        return []
