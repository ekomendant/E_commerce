def test_smartphone(prod_smartphone_1):
    assert prod_smartphone_1.name == "Iphone 15"
    assert prod_smartphone_1.description == "512GB, Gray space"
    assert prod_smartphone_1.price == 210000.0
    assert prod_smartphone_1.quantity == 8
    assert prod_smartphone_1.efficiency == 98.2
    assert prod_smartphone_1.model == "15"
    assert prod_smartphone_1.memory == 512
    assert prod_smartphone_1.color == "Gray space"
