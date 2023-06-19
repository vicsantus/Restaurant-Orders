import pytest
from src.models.ingredient import Ingredient
from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    # Mock
    teste1 = Dish("Jorge", 20.0)
    teste2 = Dish("Bruno", 13.0)
    ingre1 = Ingredient("presunto")

    # Teste funcionamento
    assert teste1 == Dish("Jorge", 20.0)

    # Teste repr
    assert repr(teste1) == f"Dish('{teste1.name}', R${teste1.price:.2f})"
    assert repr(teste1) != f"Dish('{teste2.name}', R${teste2.price:.2f})"

    # Teste hash
    assert hash(teste1) == hash(Dish("Jorge", 20.0))
    assert hash(teste1) != hash(teste2)

    # Teste name e price
    assert teste1.name == "Jorge"
    assert teste1.price == 20.0

    # Teste eq
    assert (teste1 == teste2) is False

    # Teste add_ingredient_dependency
    teste1.add_ingredient_dependency(ingre1, 2)
    assert teste1.recipe == {ingre1: 2}

    # Teste get_ingredients
    assert teste1.get_ingredients() == {ingre1}

    # Teste get_restrictions
    assert teste1.get_restrictions() == ingre1.restrictions

    # Teste erros no argumento
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Padawan", "x")
    with pytest.raises(ValueError,
                       match="Dish price must be greater then zero."):
        Dish("Apprentice becomes master", -1)
