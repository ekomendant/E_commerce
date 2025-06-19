def test_lawn_grass(prod_lawngrass_1):
    assert prod_lawngrass_1.name == "Газонная трава"
    assert prod_lawngrass_1.description == "Элитная трава для газона"
    assert prod_lawngrass_1.price == 500.0
    assert prod_lawngrass_1.quantity == 20
    assert prod_lawngrass_1.country == "Россия"
    assert prod_lawngrass_1.germination_period == "7 дней"
    assert prod_lawngrass_1.color == "Зеленый"
