import pytest


def test_iterator(iterator):
    iter(iterator)
    assert iterator.index == 0
    assert next(iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(iterator).name == "Iphone 15"
    assert next(iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(iterator)
