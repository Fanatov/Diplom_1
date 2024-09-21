from DATA import *


def test_burger_constructor_bun(burger, mock_bun):
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun


def test_burger_constructor_ingridient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    assert burger.ingredients[0] == mock_ingredient


def test_add_ingredient(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    assert len(burger.ingredients) == 1


def test_remove_ingredient(burger_complete):
    burger_complete.remove_ingredient(0)
    assert len(burger_complete.ingredients) == 0


def test_move_ingredient(burger_complete, mock_ingredient_2):
    burger_complete.add_ingredient(mock_ingredient_2)
    burger_complete.move_ingredient(0, 1)
    assert burger_complete.ingredients[0] is mock_ingredient_2


def test_get_price(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    actual_price = burger.get_price()
    expected_price = mock_bun.get_price() * 2 + mock_ingredient.get_price()
    assert actual_price == expected_price


def test_get_receipt(burger_complete):
    receipt = burger_complete.get_receipt()
    expected_receipt = f'(==== {Buns.WHITE_BUN} ====)\n= sauce {Ingridients.HOT_SAUCE} =\n(==== {Buns.WHITE_BUN} ====)\n\nPrice: {burger_complete.get_price()}'
    assert receipt == expected_receipt
