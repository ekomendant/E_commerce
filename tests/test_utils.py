from json import JSONDecodeError
from unittest.mock import patch

from src.utils import create_objects_from_json, read_json

""" Тестирование функции src.utils.read_json """


# Проверка успешного открытия и чтения JSON-файла
@patch("builtins.open")
@patch(
    "json.load",
    return_value=[{"name": "Смартфоны", "description": "Умные устройства"}],
)
def test_read_json_success(mock_load, mock_open):
    file = mock_open.return_value.__enter__.return_value
    assert read_json("test_file.json") == [{"name": "Смартфоны", "description": "Умные устройства"}]

    mock_open.assert_called_once_with("test_file.json", "r", encoding="utf-8")
    mock_load.assert_called_once_with(file)


# Проверка функции, если файл пустой
@patch("builtins.open")
@patch("json.load", side_effect=JSONDecodeError("Expecting value", "", 0))
def test_read_json_no_data(mock_load, mock_open):
    file = mock_open.return_value.__enter__.return_value
    assert read_json("test_file.json") == []

    mock_open.assert_called_once_with("test_file.json", "r", encoding="utf-8")
    mock_load.assert_called_once_with(file)


# Проверка функции, если файл не найден
@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_json_no_file(mock_open):
    assert read_json("test_file.json") == []


""" Тестирование функции src.utils.read_json """


def test_create_objects_from_json(category_from_json, second_category):
    result = create_objects_from_json(category_from_json)

    # Проверка успешного создания класса Category
    assert result[0].name == second_category.name
    assert result[0].description == second_category.description
    assert len(result[0].products) == len(second_category.products)

    # Проверка успешного создания класса Product
    assert result[0].products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'

    # Проверка, если данные на входе не соответствуют нужному формату
    assert create_objects_from_json([]) == []
    assert create_objects_from_json(1) == []
